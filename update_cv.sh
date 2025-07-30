#!/bin/bash

# CV Update Script
# Automatically downloads CV from Google Docs and replaces the local file

set -e  # Exit on any error

# Configuration
GOOGLE_DOC_ID="1BtkcTFTMQb9OcFOpM2-ex3Ynm31VcJPaItTDGnZACAQ"
CV_FILENAME="boaz_sobrado_cv.pdf"
STATIC_DIR="static"
TEMP_FILE="temp_cv.pdf"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}🔄 Starting CV update process...${NC}"

# Check if we're in the correct directory
if [ ! -d "$STATIC_DIR" ]; then
    echo -e "${RED}❌ Error: $STATIC_DIR directory not found. Please run this script from the root of your Hugo site.${NC}"
    exit 1
fi

# Construct the Google Docs export URL
DOWNLOAD_URL="https://docs.google.com/document/d/${GOOGLE_DOC_ID}/export?format=pdf"

echo -e "${YELLOW}📥 Downloading CV from Google Docs...${NC}"

# Download the PDF with curl
if curl -L -o "$TEMP_FILE" "$DOWNLOAD_URL"; then
    echo -e "${GREEN}✅ Successfully downloaded CV${NC}"
else
    echo -e "${RED}❌ Failed to download CV from Google Docs${NC}"
    exit 1
fi

# Check if the downloaded file is actually a PDF
if file "$TEMP_FILE" | grep -q "PDF"; then
    echo -e "${GREEN}✅ Downloaded file is a valid PDF${NC}"
else
    echo -e "${RED}❌ Downloaded file is not a valid PDF${NC}"
    rm -f "$TEMP_FILE"
    exit 1
fi

# Backup the existing CV (optional)
if [ -f "$STATIC_DIR/$CV_FILENAME" ]; then
    cp "$STATIC_DIR/$CV_FILENAME" "$STATIC_DIR/${CV_FILENAME}.backup"
    echo -e "${YELLOW}📋 Created backup of existing CV${NC}"
fi

# Replace the existing CV
mv "$TEMP_FILE" "$STATIC_DIR/$CV_FILENAME"
echo -e "${GREEN}✅ CV successfully updated at $STATIC_DIR/$CV_FILENAME${NC}"

# Show file info
echo -e "${YELLOW}📊 File information:${NC}"
ls -lh "$STATIC_DIR/$CV_FILENAME"

# Optional: Rebuild the site (uncomment if you want automatic rebuild)
# echo -e "${YELLOW}🔨 Rebuilding Hugo site...${NC}"
# hugo --minify

echo -e "${GREEN}🎉 CV update completed successfully!${NC}"
echo -e "${YELLOW}💡 Next steps:${NC}"
echo -e "   1. Review the updated CV at $STATIC_DIR/$CV_FILENAME"
echo -e "   2. Test locally with: hugo server"
echo -e "   3. Commit and push changes to deploy"