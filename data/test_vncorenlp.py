from vncorenlp import VnCoreNLP

# To perform word segmentation, POS tagging, NER and then dependency parsing
annotator = VnCoreNLP("/hdd/Zalo_Team_HoaChan/resources/VnCoreNLP/VnCoreNLP-1.1.1.jar", annotators="wseg,pos,ner,parse", max_heap_size='-Xmx2g')

# To perform word segmentation, POS tagging and then NER
# annotator = VnCoreNLP("<FULL-PATH-to-VnCoreNLP-jar-file>", annotators="wseg,pos,ner", max_heap_size='-Xmx2g')
# To perform word segmentation and then POS tagging
# annotator = VnCoreNLP("<FULL-PATH-to-VnCoreNLP-jar-file>", annotators="wseg,pos", max_heap_size='-Xmx2g')
# To perform word segmentation only
# annotator = VnCoreNLP("<FULL-PATH-to-VnCoreNLP-jar-file>", annotators="wseg", max_heap_size='-Xmx500m')

# Input
text = "Tuy vậy, 1 phút sau, Chelsea đã cụ thể hóa sức ép liên tục bằng bàn thắng. Người lập công cho The Blues là đội trưởng Cahill với cú đánh đầu cận thành từ tình huống phạt góc."

# To perform word segmentation, POS tagging, NER and then dependency parsing
annotated_text = annotator.annotate(text)

# To perform word segmentation only
word_segmented_text = annotator.tokenize(text)

print('annotated_text: ', annotated_text)
print('word_segmented_text: ', word_segmented_text)

{'index': 7, 'form': 'Cahill', 'posTag': 'Np', 'nerLabel': 'B-PER', 'head': 6, 'depLabel': 'nmod'}