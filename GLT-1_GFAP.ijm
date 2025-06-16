input_path = getDirectory("Choose your data to be analyzed");
output_path = getDirectory("Select destination directory for your intensity data");
fileList = getFileList(input_path) 

for (f = 0; f<fileList.length; f++){
		
		open(input_path + fileList[f]); 
		run("Z Project...", "projection=[Max Intensity]");
		Stack.getDimensions(width, height, channels, slices, frames); 
		title = getTitle();
		run("Set Measurements...", "area mean integrated redirect=None decimal=3");
		if (channels == 2) {
			run("Split Channels");
			selectWindow ("C1-" + title);
			rename("GLT");
			selectWindow ("C2-" + title);
			rename("GFAP");

			//Getting infos about whole GLT1
	        selectWindow("GLT");
	        run("Measure");
	        selectWindow("Results");
	        saveAs("Results", output_path + title + "-GLT_whole.csv");
	        run("Close");
			
			// Duplicate GFAP channel
	        selectWindow("GFAP");
	        run("Duplicate...", "title=GFAP_threshold"); 
	
	        // Enhance Contrast of GFAP
	        selectWindow("GFAP_threshold");
	        run("Enhance Contrast", "saturated=0.35");
	        
	        // Thresholding of Astrocytes
	        selectWindow("GFAP_threshold");
	        setAutoThreshold("Huang dark");
	        setOption("BlackBackground", false);
	        run("Convert to Mask");
	        selectWindow("GFAP_threshold");
	        run("Create Selection");
	        
	        //Getting infos about GFAP
	        selectWindow("GFAP");
	        run("Restore Selection");
	        selectImage("GFAP");
	        run("Measure");
	
	        // Save your data (Astrocytes inside scratch using original GFAP image)
	        selectWindow("Results");
	        saveAs("Results", output_path + title + "-GFAP.csv");
	        run("Close");
	        
	        //Getting infos about GLT
	        selectWindow("GLT");
	        run("Restore Selection");
	        selectImage("GLT");
	        run("Measure");
	
	        // Save your data (Astrocytes inside scratch using original GFAP image)
	        selectWindow("Results");
	        saveAs("Results", output_path + title + "-GLT.csv");
	        run("Close");
	        
	        //Save GFAP threshold
	        selectWindow("GFAP_threshold");
	        saveAs("PNG", output_path + title + "-GFAP_Threshold.png");
	        run("Close");
	        
	        roiManager("reset");

		}
		
		if (channels == 3) {
			run("Split Channels");
			selectWindow ("C1-" + title);
			run("Close");
			selectWindow ("C2-" + title);
			rename("GLT");
			selectWindow ("C3-" + title);
			rename("GFAP");

			//Getting infos about whole GLT1
	        selectWindow("GLT");
	        run("Measure");
	        selectWindow("Results");
	        saveAs("Results", output_path + title + "-GLT_whole.csv");
	        run("Close");
			
			// Duplicate GFAP channel
	        selectWindow("GFAP");
	        run("Duplicate...", "title=GFAP_threshold"); 
	
	        // Enhance Contrast of GFAP
	        selectWindow("GFAP_threshold");
	        run("Enhance Contrast", "saturated=0.35");
	        
	        // Thresholding of Astrocytes
	        selectWindow("GFAP_threshold");
	        setAutoThreshold("Huang dark");
	        setOption("BlackBackground", false);
	        run("Convert to Mask");
	        selectWindow("GFAP_threshold");
	        run("Create Selection");
	        
	        //Getting infos about GFAP
	        selectWindow("GFAP");
	        run("Restore Selection");
	        selectImage("GFAP");
	        run("Measure");
	
	        // Save your data (Astrocytes inside scratch using original GFAP image)
	        selectWindow("Results");
	        saveAs("Results", output_path + title + "-GFAP.csv");
	        run("Close");
	        
	        //Getting infos about GLT
	        selectWindow("GLT");
	        run("Restore Selection");
	        selectImage("GLT");
	        run("Measure");
	
	        // Save your data (Astrocytes inside scratch using original GFAP image)
	        selectWindow("Results");
	        saveAs("Results", output_path + title + "-GLT.csv");
	        run("Close");
	        
	        //Save GFAP threshold
	        selectWindow("GFAP_threshold");
	        saveAs("PNG", output_path + title + "-GFAP_Threshold.png");
	        run("Close");
	        
	        roiManager("reset");

		}
		
		if (channels == 4) {
			run("Split Channels");
			selectWindow ("C1-" + title);
			run("Close");
			selectWindow ("C2-" + title);
			run("Close");
			selectWindow ("C3-" + title);
			rename("GLT");
			selectWindow ("C4-" + title);
			rename("GFAP");
			
			//Getting infos about whole GLT1
	        selectWindow("GLT");
	        run("Measure");
	        selectWindow("Results");
	        saveAs("Results", output_path + title + "-GLT_whole.csv");
	        run("Close");
			
			// Duplicate GFAP channel
	        selectWindow("GFAP");
	        run("Duplicate...", "title=GFAP_threshold"); 
	
	        // Enhance Contrast of GFAP
	        selectWindow("GFAP_threshold");
	        run("Enhance Contrast", "saturated=0.35");
	        
	        // Thresholding of Astrocytes
	        selectWindow("GFAP_threshold");
	        setAutoThreshold("Huang dark");
	        setOption("BlackBackground", false);
	        run("Convert to Mask");
	        selectWindow("GFAP_threshold");
	        run("Create Selection");
	        
	        //Getting infos about GFAP
	        selectWindow("GFAP");
	        run("Restore Selection");
	        selectImage("GFAP");
	        run("Measure");
	
	        // Save your data (Astrocytes inside scratch using original GFAP image)
	        selectWindow("Results");
	        saveAs("Results", output_path + title + "-GFAP.csv");
	        run("Close");
	        
	        //Getting infos about GLT
	        selectWindow("GLT");
	        run("Restore Selection");
	        selectImage("GLT");
	        run("Measure");
	
	        // Save your data (Astrocytes inside scratch using original GFAP image)
	        selectWindow("Results");
	        saveAs("Results", output_path + title + "-GLT.csv");
	        run("Close");
	        
	        //Save GFAP threshold
	        selectWindow("GFAP_threshold");
	        saveAs("PNG", output_path + title + "-GFAP_Threshold.png");
	        run("Close");
	        
	        roiManager("reset");

		}
		
		
//Clean-up to prepare for next image
	roiManager("reset");
	run("Close All");
	run("Clear Results");
	close("*");
	
	if (isOpen("Log")) {
         selectWindow("Log");
         run("Close");
	}
	if (isOpen("Summary")) {
         selectWindow("Summary");
         run("Close");
	}
	
		
}
print("Jeah, finished!");