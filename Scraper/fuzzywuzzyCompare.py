from fuzzywuzzy import fuzz
import cv2
import requests
from io import BytesIO
import numpy as np
from skimage.metrics import structural_similarity as ssim
from scipy import signal
from scipy.ndimage import uniform_filter

def compare(safewayList, superstoreList, noFrillsList, igaList, walmartList, saveOnList, query, province_id, DEBUG=False):    

    groups = []
    groupID = 1
    
    groceryList = [safewayList, superstoreList, noFrillsList, igaList, walmartList, saveOnList]

    for itemList in groceryList:
        
        for item in itemList:
            
            igaMax = 0
            igaProduct = ""
            igaBrand = ""
            
            safewayMax = 0
            safewayProduct = ""
            safewayBrand = ""
            
            walmartMax = 0
            walmartProduct = ""
            walmartBrand = ""
            
            saveOnMax = 0
            saveOnProduct = ""
            saveOnBrand = ""
            
            noFrillsMax = 0
            noFrillsProduct = ""
            noFrillsBrand = ""
            
            superstoreMax = 0
            superstoreProduct = ""
            superstoreBrand = ""
        
            for safeway in safewayList:
                if item["merchant"].lower() == "safeway":
                    break
                
                if safeway["brand"] != None and item["brand"] != None:
                    
                    #print(compare_images(image1, image2))
                    
                    if fuzz.ratio(safeway["brand"].lower(), item["brand"].lower()) > 80:
                        similarity_ratio = fuzz.ratio(iga["name"], item["name"])
                        url = item["image_link"]
                        if url != None:
                            response = requests.get(url)
                            image_data = BytesIO(response.content)
                            
                            image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                            image1 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                            
                        url = safeway["image_link"]
                        if url != None:
                            response = requests.get(url)
                            image_data = BytesIO(response.content)
                            
                            image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                            image2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                            
                        imageComparison = compare_images(image1, image2)
                        if similarity_ratio + 2*imageComparison > igaMax:                         
                            safewayMax = similarity_ratio + imageComparison
                            safewayProduct = iga["name"]
                            safewayBrand = iga["brand"]
                            safewayItem = safeway
            
            for iga in igaList:
                
                if item["merchant"].lower() == "iga":
                    break
                if iga["brand"] != None and item["brand"] != None:
                
                    if fuzz.ratio(iga["brand"].lower(), item["brand"].lower()) > 80:
                        similarity_ratio = fuzz.ratio(iga["name"], item["name"])
                        url = item["image_link"]
                        if url != None:
                            response = requests.get(url)
                            image_data = BytesIO(response.content)
                            
                            image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                            image1 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                            
                        url = iga["image_link"]
                        if url != None:
                            response = requests.get(url)
                            image_data = BytesIO(response.content)
                            
                            image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                            image2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                            
                        imageComparison = compare_images(image1, image2)
                        if similarity_ratio + 2*imageComparison > igaMax:
                            igaMax = similarity_ratio
                            igaProduct = iga["name"]
                            igaBrand = iga["brand"]
                            igaItem = iga

            #print(f"item Product: {item}")
            #print(f"IGA Product: {igaProduct}")
            #print(f"IGA Brand: {igaBrand}")
            #print(f"Similarity Ratio: {igaMax}")
            
            for noFrills in noFrillsList:
                
                if item["merchant"].lower() == "nofrills":
                    break
                
                if noFrills["brand"] != None and item["brand"] != None:
                
                    if noFrills["brand"] != None and item["brand"] != None:
                        if fuzz.ratio(noFrills["brand"].lower(), item["brand"].lower()) > 80:
                            similarity_ratio = fuzz.ratio(noFrills["name"], item["name"])
                            url = item["image_link"]
                            if url != None:
                                response = requests.get(url)
                                image_data = BytesIO(response.content)
                                
                                image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                                image1 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            url = noFrills["image_link"]
                            if url != None:
                                response = requests.get(url)
                                image_data = BytesIO(response.content)
                                
                                image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                                image2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            imageComparison = compare_images(image1, image2)
                            if similarity_ratio + 2*imageComparison > noFrillsMax:
                                noFrillsMax = similarity_ratio
                                noFrillsProduct = noFrills["name"]
                                noFrillsBrand = noFrills["brand"]
                                noFrillsItem = noFrills

            #print(f"item Product: {item}")
            #print(f"NoFrills Product: {noFrillsProduct}")
            #print(f"NoFrills Brand: {noFrillsBrand}")
            #print(f"Similarity Ratio: {noFrillsMax}")
            
            for superstore in superstoreList:
                
                if item["merchant"].lower() == "superstore":
                    break
                
                if superstore["brand"] != None and item["brand"] != None:

                    if superstore["brand"] != None and item["brand"] != None:
                        if fuzz.ratio(superstore["brand"].lower(), item["brand"].lower()) > 80:
                            similarity_ratio = fuzz.ratio(superstore["name"], item["name"])
                            url = item["image_link"]
                            if url != None:
                                response = requests.get(url)
                                image_data = BytesIO(response.content)
                                
                                image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                                image1 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            url = superstore["image_link"]
                            if url != None:
                                response = requests.get(url)
                                image_data = BytesIO(response.content)
                                
                                image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                                image2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            imageComparison = compare_images(image1, image2)
                            if similarity_ratio + 2*imageComparison > superstoreMax:
                                superstoreMax = similarity_ratio
                                superstoreProduct = superstore["name"]
                                superstoreBrand = superstore["brand"]
                                superstoreItem = superstore

            #print(f"item Product: {item}")
            #print(f"Superstore Product: {superstoreProduct}")
            #print(f"Superstore Brand: {superstoreBrand}")
            #print(f"Similarity Ratio: {superstoreMax}")
            
            for walmart in walmartList:
                
                if item["merchant"].lower() == "walmart":
                    break
                
                if walmart["brand"] != None and item["brand"] != None:
                
                    if walmart["brand"] != None and item["brand"] != None:
                        if fuzz.ratio(walmart["brand"].lower(), item["brand"].lower()) > 80:
                            similarity_ratio = fuzz.ratio(walmart["name"], item["name"])
                            url = item["image_link"]
                            if url != None:
                                response = requests.get(url)
                                image_data = BytesIO(response.content)
                                
                                image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                                image1 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            url = walmart["image_link"]
                            if url != None:
                                response = requests.get(url)
                                image_data = BytesIO(response.content)
                                
                                image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                                image2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            imageComparison = compare_images(image1, image2)
                            if similarity_ratio + 2*imageComparison > walmartMax:
                                walmartMax = similarity_ratio
                                walmartProduct = walmart["name"]
                                walmartBrand = walmart["brand"]
                                walmartItem = walmart
                            
            for saveOn in saveOnList:
                
                if item["merchant"] == "Save-On-Foods":
                    break
                
                if saveOn["brand"] != None and item["brand"] != None:
                
                    if saveOn["brand"] != None and item["brand"] != None:
                        if fuzz.ratio(saveOn["brand"].lower(), item["brand"].lower()) > 80:
                            similarity_ratio = fuzz.ratio(saveOn["name"], item["name"])
                            url = item["image_link"]
                            if url != None:
                                response = requests.get(url)
                                image_data = BytesIO(response.content)
                                
                                image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                                image1 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            url = saveOn["image_link"]
                            if url != None:
                                response = requests.get(url)
                                image_data = BytesIO(response.content)
                                
                                image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                                image2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            imageComparison = compare_images(image1, image2)
                            if similarity_ratio + 2*imageComparison > saveOnMax:
                                saveOnMax = similarity_ratio
                                saveOnProduct = saveOn["name"]
                                saveOnBrand = saveOn["brand"]
                                saveOnItem = saveOn
            
            group = {}
            
            products = []
            
            if safewayMax >= 50:
                products.append(safeway)
            
            if igaMax >= 50:
                products.append(igaItem)
                
            if noFrillsMax >= 50:
                products.append(noFrillsItem)
                
            if superstoreMax >= 50:
                products.append(superstoreItem)
                
            if walmartMax >= 50:
                products.append(walmartItem)
                
            if saveOnMax >= 50:
                products.append(saveOnItem)
                
            group["groupID"] = groupID
            group["search_string"] = query
            group["products"] = products
            
            if len(group["products"]) >= 1:
            
                groupList.append(group)
            
                groupID += 1
    
    groupList = {
        'search_query' : query,
        'province_id' : province_id,
        'groups' : groups
    }

    if(DEBUG):
        print(groupList)
    return groupList


#Thanks Chat
def ssim(image1, image2, win_size=11, L=255):
    # Ensure images are numpy arrays
    image1 = np.array(image1)
    image2 = np.array(image2)

    # Calculate constants for SSIM
    K1 = 0.01
    K2 = 0.03
    C1 = (K1 * L) ** 2
    C2 = (K2 * L) ** 2

    # Calculate means, variances, and covariances
    mu1 = uniform_filter(image1, win_size)
    mu2 = uniform_filter(image2, win_size)
    mu1_sq = mu1 * mu1
    mu2_sq = mu2 * mu2
    mu12 = mu1 * mu2
    sigma1_sq = uniform_filter(image1 * image1, win_size) - mu1_sq
    sigma2_sq = uniform_filter(image2 * image2, win_size) - mu2_sq
    sigma12 = uniform_filter(image1 * image2, win_size) - mu12

    # Calculate SSIM
    num = (2 * mu12 + C1) * (2 * sigma12 + C2)
    den = (mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2)
    ssim_map = num / den
    ssim_score = np.mean(ssim_map)

    return ssim_score

def compare_images(image1, image2):
    # Load images
    if isinstance(image1, str):
        image1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE)
    if isinstance(image2, str):
        image2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE)

    # Resize the smaller image to match the dimensions of the larger image
    if image1.shape != image2.shape:
        min_height = min(image1.shape[0], image2.shape[0])
        min_width = min(image1.shape[1], image2.shape[1])
        image1 = cv2.resize(image1, (min_width, min_height), interpolation=cv2.INTER_LINEAR)
        image2 = cv2.resize(image2, (min_width, min_height), interpolation=cv2.INTER_LINEAR)

    # Compute SSIM
    similarity_score = ssim(image1, image2)
    return similarity_score