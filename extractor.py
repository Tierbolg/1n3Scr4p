import config.PROPERTIES as PROPERTIES
import helper.common as helperCommon

if __name__ == '__main__':
    codigosUrl=[]
    codigosUrl= helperCommon.buscarcodigos()
    for urlDeExcel in codigosUrl:
        helperCommon.get_page(urlDeExcel)
        
