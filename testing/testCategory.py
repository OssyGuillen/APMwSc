# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo category.py
sys.path.append('../app/scrum')

from category import *

class TestCategory(unittest.TestCase):
    
    #############################################      
    #         Pruebas para insertCategory       #
    #############################################
    
    # Caso Inicial
  
    # Prueba 1
    def testInsertCategory(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzry1',21)
 
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzry1')
         
    # Casos Frontera
     
    # Prueba 2
    def testInsertCategoryExists(self):
        aCategory = category()
        result    = aCategory.insertCategory('Kxtygzry1',21)
        self.assertTrue(result)
 
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzry1')
         
    # Prueba 3
    def testInsertCategory1Exists(self):
        aCategory = category()
        result    = aCategory.insertCategory('A',1)
        self.assertTrue(result)
 
        # Eliminando la categoria
        aCategory.deleteCategory('A')
         
    # Prueba 4
    def testInsertCategory100Exists(self):
        aCategory = category()
        result    = aCategory.insertCategory('A'*100,2)
        self.assertTrue(result)
 
        # Eliminando la categoria
        aCategory.deleteCategory('A'*100)
         
    # Prueba 5
    def testInsertCategory0Exists(self):
        aCategory = category()
        result    = aCategory.insertCategory('',1)
        self.assertFalse(result)
 
    # Prueba 6
    def testInsertCategory101Exists(self):
        aCategory = category()
        result    = aCategory.insertCategory('A'*101,1)
        self.assertFalse(result)
 
    # Prueba 7
    def testInsertCategoryLongExists(self):
        aCategory = category()
        result    = aCategory.insertCategory('A'*((2**28)-1),1)
        self.assertFalse(result)
         
    # Prueba 8
    def testInsertCategoryEquals(self):
        aCategory = category()
        result    = aCategory.insertCategory('Kxtygzrda',2)
        result1   = aCategory.insertCategory('Kxtygzrda',3)
        self.assertFalse(result1)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
         
    # Prueba 9
    def testInsertCategory1Equals(self):
        aCategory = category()
        result    = aCategory.insertCategory('C',2)
        result1   = aCategory.insertCategory('C',3)
        self.assertFalse(result1)
         
        # Eliminando la categoria
        aCategory.deleteCategory('C')
     
    # Prueba 10
    def testInsertCategory100Equals(self):
        aCategory = category()
        result    = aCategory.insertCategory('C'*100,2)
        result1   = aCategory.insertCategory('C'*100,3)
        self.assertFalse(result1)
         
        # Eliminando la categoria
        aCategory.deleteCategory('C'*100)
         
    # Prueba 11
    def testInsertCategoryWeight1(self):
        aCategory = category()
        result    = aCategory.insertCategory('Kxtygzrda',1)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
         
    # Prueba 12
    def testInsertCategoryWeight50(self):
        aCategory = category()
        result    = aCategory.insertCategory('Kxtygzrda',((2**28)-1))
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
         
    # Prueba 13
    def testInsertCategoryWeight0(self):
        aCategory = category()
        result    = aCategory.insertCategory('Kxtygzrda',0)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
         
    # Casos Esquina
     
    # Prueba 14
    def testInsertCategoryName0Weight0(self):
        aCategory = category()
        result    = aCategory.insertCategory('',0)
        self.assertFalse(result)
         
    # Prueba 15
    def testInsertCategoryName1Weight0(self):
        aCategory = category()
        result    = aCategory.insertCategory('A',0)
        self.assertTrue(result)
 
        # Eliminando la categoria
        aCategory.deleteCategory('A')
         
    # Prueba 16
    def testInsertCategoryName100Weight0(self):
        aCategory = category()
        result    = aCategory.insertCategory('A'*100,0)
        self.assertTrue(result)
 
        # Eliminando la categoria
        aCategory.deleteCategory('A'*100)
         
    # Prueba 17
    def testInsertCategoryName1WeightLong(self):
        aCategory = category()
        result    = aCategory.insertCategory('A',((2**28)-1))
        self.assertTrue(result)
 
        # Eliminando la categoria
        aCategory.deleteCategory('A')
         
    # Prueba 18
    def testInsertCategoryName0WeightLong(self):
        aCategory = category()
        result    = aCategory.insertCategory('',((2**28)-1))
        self.assertFalse(result)
         
    # Casos Malicia
     
    # Prueba 19
    def testInsertCategorySpaceExists(self):
        aCategory = category()
        result    = aCategory.insertCategory(' ',2)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory(' ')
         
    # Prueba 20
    def testInsertCategoryEnieExists(self):
        aCategory = category()
        result    = aCategory.insertCategory('ñ',2)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('ñ')
         
    # Prueba 21
    def testInsertCategoryNumber(self):
        aCategory = category()
        result    = aCategory.insertCategory(12,2)
        self.assertFalse(result)
 
    # Prueba 22
    def testInsertCategoryArray(self):
        aCategory = category()
        result    = aCategory.insertCategory([],2)
        self.assertFalse(result)
         
    # Prueba 23
    def testInsertCategoryDictionari(self):
        aCategory = category()
        result    = aCategory.insertCategory({},2)
        self.assertFalse(result)
         
    # Prueba 24
    def testInsertCategoryWeightString(self):
        aCategory = category()
        result    = aCategory.insertCategory('kxtygzrya','1')
        self.assertFalse(result)
     
    # Prueba 25
    def testInsertCategoryWeightArray(self):
        aCategory = category()
        result    = aCategory.insertCategory('kxtygzrya',[])
        self.assertFalse(result)
          
    # Prueba 26
    def testInsertCategoryWeightDictionari(self):
        aCategory = category()
        result    = aCategory.insertCategory('kxtygzrya',{})
        self.assertFalse(result)
         
     
    #############################################      
    #        Pruebas para updateCategory        #
    #############################################
     
    # Caso Normal
     
    # Prueba 27
    def testUpdateCategoryExist(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.updateCategory('Kxtygzrda', 'Nxyvz kxtygzrya', 2)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Nxyvz kxtygzrya')
         
    # Prueba 28
    def testUpdateCategoryNotExist(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.updateCategory('kxty', 'Nxyvz kxtygzrya', 2)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
         
    # Casos Frontera
     
    # Prueba 29
    def testUpdateCategoryName1Newname1(self):
        aCategory = category()
        aCategory.insertCategory('C',1)
        result    = aCategory.updateCategory('C', 'N', 2)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('N')
         
    # Prueba 30
    def testUpdateCategoryName1Newname(self):
        aCategory = category()
        aCategory.insertCategory('C',1)
        result    = aCategory.updateCategory('C', 'Nxyvz kxtygzrya', 2)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Nxyvz kxtygzrya') 
         
    # Prueba 31
    def testUpdateCategoryName0(self):
        aCategory = category()
        aCategory.insertCategory('',1)
        result    = aCategory.updateCategory('', 'N', 2)
        self.assertFalse(result)
         
    # Prueba 32
    def testUpdateCategoryNameNewname1(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.updateCategory('Kxtygzrda', 'N', 2)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('N')
         
    # Prueba 33
    def testUpdateCategoryName100Newname(self):
        aCategory = category()
        aCategory.insertCategory('C'*100,1)
        result    = aCategory.updateCategory('C'*100, 'Nxyvz kxtygzrya', 2)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Nxyvz kxtygzrya')
         
    # Prueba 34
    def testUpdateCategoryNameNewname100(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.updateCategory('Kxtygzrda', 'N'*100, 2)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('N'*100)
     
    # Prueba 35
    def testUpdateCategoryNewname101(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.updateCategory('C', 'N'*101, 2)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
         
    # Prueba 36
    def testUpdateCategoryNameNewname0(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.updateCategory('Kxtygzrda', '', 2)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
         
    # Prueba 37
    def testUpdateCategoryNewnameLong(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.updateCategory('Kxtygzrda', 'N'*((2**28)-1), 2)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
         
    # Prueba 38
    def testUpdateCategoryWeight0(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.updateCategory('Kxtygzrda', 'Nxyvz kxtygzrya', 0)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Nxyvz kxtygzrya')
         
    # Prueba 39
    def testUpdateCategoryWeightLong(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.updateCategory('Kxtygzrda', 'Nxyvz kxtygzrya', ((2**28)-1))
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Nxyvz kxtygzrya')
         
    # Casos Esquina
     
    # Prueba 40
    def testUpdateCategoryName0Newname0Weight0(self):
        aCategory = category()
        aCategory.insertCategory('',1)
        result    = aCategory.updateCategory('', '', 0)
        self.assertFalse(result)
 
    # Prueba 41
    def testUpdateCategoryName1Newname0Weight0(self):
        aCategory = category()
        aCategory.insertCategory('C',1)
        result    = aCategory.updateCategory('C', '', 0)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
         
    # Prueba 42
    def testUpdateCategoryName100Newname0Weight0(self):
        aCategory = category()
        aCategory.insertCategory('C'*100,1)
        result    = aCategory.updateCategory('C'*100, '', 0)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('C'*100)
         
    # Prueba 43
    def testUpdateCategoryNameLongNewname0Weight0(self):
        aCategory = category()
        aCategory.insertCategory('C'*((2**28)-1),1)
        result    = aCategory.updateCategory('C'*((2**28)-1), '', 0)
        self.assertFalse(result)
         
    # Prueba 44
    def testUpdateCategoryName0Newname1Weight0(self):
        aCategory = category()
        aCategory.insertCategory('',1)
        result    = aCategory.updateCategory('', 'N', 0)
        self.assertFalse(result)
             
    # Prueba 45
    def testUpdateCategoryName0Newname100Weight0(self):
        aCategory = category()
        aCategory.insertCategory('',1)
        result    = aCategory.updateCategory('', 'N'*100, 0)
        self.assertFalse(result)
 
    # Prueba 46
    def testUpdateCategoryName0NewnameLongWeight0(self):
        aCategory = category()
        aCategory.insertCategory('',1)
        result    = aCategory.updateCategory('', 'N'*((2**28)-1), 0)
        self.assertFalse(result)
         
    # Prueba 47
    def testUpdateCategoryName0Newname0Weight1(self):
        aCategory = category()
        aCategory.insertCategory('',1)
        result    = aCategory.updateCategory('', '', 1)
        self.assertFalse(result)
         
    # Prueba 48
    def testUpdateCategoryName0Newname0WeightLong(self):
        aCategory = category()
        aCategory.insertCategory('',1)
        result    = aCategory.updateCategory('', '', (2**28)-1)
        self.assertFalse(result)
         
    # Prueba 49
    def testUpdateCategoryName1Newname1WeightLong1(self):
        aCategory = category()
        aCategory.insertCategory('C',1)
        result    = aCategory.updateCategory('C', 'N', 1)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('N')
         
    # Prueba 50
    def testUpdateCategoryName100Newname1WeightLong1(self):
        aCategory = category()
        aCategory.insertCategory('C'*100,1)
        result    = aCategory.updateCategory('C'*100, 'N', 1)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('N')
         
    # Prueba 51
    def testUpdateCategoryNameLongNewname1WeightLong1(self):
        aCategory = category()
        aCategory.insertCategory('C'*((2**28)-1),1)
        result    = aCategory.updateCategory('C'*((2**28)-1), 'N', 1)
        self.assertFalse(result)
           
    # Prueba 52
    def testUpdateCategoryName1Newname100WeightLong1(self):
        aCategory = category()
        aCategory.insertCategory('C',1)
        result    = aCategory.updateCategory('C', 'N'*100, 1)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('N'*100)
         
    # Prueba 53
    def testUpdateCategoryName1NewnameLongWeightLong1(self):
        aCategory = category()
        aCategory.insertCategory('C',1)
        result    = aCategory.updateCategory('C', 'N'*((2**28)-1), 1)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('C')
         
    # Prueba 54
    def testUpdateCategoryName1Newname1WeightLong(self):
        aCategory = category()
        aCategory.insertCategory('C',1)
        result    = aCategory.updateCategory('C', 'N', (2**28)-1)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('N')
         
    # Prueba 55
    def testUpdateCategoryName100Newname100WeightLong(self):
        aCategory = category()
        aCategory.insertCategory('C'*100,1)
        result    = aCategory.updateCategory('C'*100, 'N'*100, (2**28)-1)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('N'*100)
         
    # Prueba 56
    def testUpdateCategoryName100NewnameLongWeightLong1(self):
        aCategory = category()
        aCategory.insertCategory('C'*100,1)
        result    = aCategory.updateCategory('C', 'N'*((2**28)-1), 1)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('C'*100)        
         
    # Casos Malicia
     
    # Prueba 57
    def testUpdateCategoryNameNewnameEnieWeight(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.updateCategory('Kxtygzrda', 'ñ', 3)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('ñ')
         
    # Prueba 58
    def testUpdateCategoryNameNewnameArrayWeight(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.updateCategory('Kxtygzrda', [], 3)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
         
    # Prueba 59
    def testUpdateCategoryNameNewnameDictionaryWeight(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.updateCategory('Kxtygzrda', {}, 3)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
         
    # Prueba 60
    def testUpdateCategoryNameNewnameNumberWeight(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.updateCategory('Kxtygzrda', 21, 3)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
         
    # Prueba 61
    def testUpdateCategoryNameNewnameWeightNegativeNumber(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.updateCategory('Kxtygzrda', 'Nxyvz kxtygzrya', -3)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
        
    #############################################      
    #       Pruebas para searchIdCategory       #
    #############################################
        
    # Caso Normal
    
    # Prueba 62
    def testSearchIdCategoryExist(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.searchIdCategory(1)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
        
    # Prueba 63
    def testSearchIdCategoryNotExist(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.searchIdCategory(99)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')    
    
    # Casos Frontera    
        
    # Prueba 64
    def testSearchIdCategory0(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.searchIdCategory(0)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')    
        
    # Prueba 65
    def testSearchIdCategoryLong(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.searchIdCategory((2**28)-1)
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
    
    # Casos Malicia
        
    # Prueba 66
    def testSearchIdCategoryString(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.searchIdCategory('0')
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
        
    # Prueba 67
    def testSearchIdCategoryArray(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.searchIdCategory([])
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
        
    # Prueba 68
    def testSearchIdCategoryDictionary(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
        result    = aCategory.searchIdCategory({})
        self.assertFalse(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Kxtygzrda')
        
    
    #############################################      
    #        Pruebas para deleteCategory        #
    #############################################
        
    # Caso Normal

    # Prueba 69
    def testDeleteCategoryExist(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
         
        # Eliminando la categoria
        result = aCategory.deleteCategory('Kxtygzrda')
        self.assertTrue(result)
        
    # Prueba 70
    def testDeleteCategoryNotExist(self):
        aCategory = category()
        aCategory.insertCategory('Kxtygzrda',1)
         
        # Eliminando la categoria
        result = aCategory.deleteCategory('Kxtyg')
        self.assertFalse(result)
        aCategory.deleteCategory('Kxtygzrda')
        
    # Casos Frontera
    
    # Prueba 71
    def testDeleteCategoryName0(self):
        aCategory = category()
        aCategory.insertCategory('',1)
         
        # Eliminando la categoria
        result = aCategory.deleteCategory('')
        self.assertFalse(result)
        
    # Prueba 72
    def testDeleteCategoryName1(self):
        aCategory = category()
        aCategory.insertCategory('C',1)
         
        # Eliminando la categoria
        result = aCategory.deleteCategory('C')
        self.assertTrue(result)
        
    # Prueba 73
    def testDeleteCategoryName50(self):
        aCategory = category()
        aCategory.insertCategory('C'*50,1)
         
        # Eliminando la categoria
        result = aCategory.deleteCategory('C'*50)
        self.assertTrue(result)
        
    # Prueba 74
    def testDeleteCategoryName101(self):
        aCategory = category()
        aCategory.insertCategory('C'*101,1)
         
        # Eliminando la categoria
        result = aCategory.deleteCategory('C'*101)
        self.assertFalse(result)
        
    # Prueba 75
    def testDeleteCategoryNameLong(self):
        aCategory = category()
        aCategory.insertCategory('C'*((2**28)-1),1)
         
        # Eliminando la categoria
        result = aCategory.deleteCategory('C'*((2**28)-1))
        self.assertFalse(result)
        
    # Casos Malicia
    
    # Prueba 76
    def testDeleteCategoryNameEnie(self):
        aCategory = category()
        aCategory.insertCategory('ñ',1)
         
        # Eliminando la categoria
        result = aCategory.deleteCategory('ñ')
        self.assertTrue(result)
        
    # Prueba 77
    def testDeleteCategoryNameNumber(self):
        aCategory = category()
        aCategory.insertCategory(88,1)
         
        # Eliminando la categoria
        result = aCategory.deleteCategory(88)
        self.assertFalse(result)
        
    # Prueba 78
    def testDeleteCategoryNameArray(self):
        aCategory = category()
        aCategory.insertCategory([],1)
         
        # Eliminando la categoria
        result = aCategory.deleteCategory([])
        self.assertFalse(result)
        
    # Prueba 79
    def testDeleteCategoryNameStringArray(self):
        aCategory = category()
        aCategory.insertCategory('[]',1)
         
        # Eliminando la categoria
        result = aCategory.deleteCategory('[]')
        self.assertTrue(result)
        
    # Prueba 80
    def testDeleteCategoryNameDictionary(self):
        aCategory = category()
        aCategory.insertCategory({},1)
         
        # Eliminando la categoria
        result = aCategory.deleteCategory({})
        self.assertFalse(result)
        
    # Prueba 81
    def testDeleteCategoryNameStringDictionary(self):
        aCategory = category()
        aCategory.insertCategory('{}',1)
         
        # Eliminando la categoria
        result = aCategory.deleteCategory('{}')
        self.assertTrue(result)

# Fin de casos de Category