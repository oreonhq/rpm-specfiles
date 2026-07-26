QT_BASE_DIR=/usr
QT_LIB_DIR=$(QT_BASE_DIR)/lib64
QT_BIN_DIR=$(QT_BASE_DIR)/bin
QT_INCLUDE_DIR=$(QT_BASE_DIR)/include

Add64: harmonics.o harmonics.moc.o \
	filter.o filter.moc.o \
	gui.o gui.moc.o \
	multislider.o multislider.moc.o \
	modslider.o modslider.moc.o \
	voicesynth.o voicesynth.moc.o \
	synth.o synth.moc.o \
	voicedata.o \
	model.o jackprocessor.o jackprocessor.moc.o main.o
	gcc -g -o Add64 \
	harmonics.o harmonics.moc.o \
	multislider.o multislider.moc.o \
	modslider.o modslider.moc.o \
	filter.o filter.moc.o \
	gui.o gui.moc.o \
	voicesynth.o voicesynth.moc.o \
	synth.o synth.moc.o \
	voicedata.o \
	model.o jackprocessor.o jackprocessor.moc.o main.o \
	-L$(QT_LIB_DIR) \
	-lQtCore -lQtGui -ljack -lm

CXXFLAGS=-I$(QT_INCLUDE_DIR) -I. -O2 -g -Wall

filter.o: filter.cpp filter.h model.h
filter.moc.o: filter.moc.cpp filter.h model.h 
filter.moc.cpp: filter.h filter.cpp
	$(QT_BIN_DIR)/moc filter.h -o filter.moc.cpp
harmonics.o: harmonics.cpp harmonics.h model.h
harmonics.moc.o: harmonics.moc.cpp harmonics.h model.h 
harmonics.moc.cpp: harmonics.h harmonics.cpp
	$(QT_BIN_DIR)/moc harmonics.h -o harmonics.moc.cpp
multislider.o: multislider.cpp multislider.h modslider.h model.h
multislider.moc.o: multislider.moc.cpp multislider.h modslider.h model.h
multislider.moc.cpp: multislider.h multislider.cpp
	$(QT_BIN_DIR)/moc multislider.h -o multislider.moc.cpp
modslider.o: modslider.cpp modslider.h model.h
modslider.moc.o: modslider.moc.cpp modslider.h model.h 
modslider.moc.cpp: modslider.h modslider.cpp
	$(QT_BIN_DIR)/moc modslider.h -o modslider.moc.cpp
midicontroller.o: midicontroller.cpp midicontroller.h
controlobject.o: controlobject.cpp controlobject.h
gui.o: gui.cpp gui.h harmonics.h synth.h model.h multislider.h modslider.h filter.h jackprocessor.h
gui.moc.o: gui.moc.cpp gui.h harmonics.h synth.h model.h multislider.h modslider.h filter.h jackprocessor.h
gui.moc.cpp: gui.h gui.cpp 
	$(QT_BIN_DIR)/moc gui.h -o gui.moc.cpp
voicesynth.o: voicesynth.cpp voicesynth.h voicedata.h model.h
voicesynth.moc.o: voicesynth.moc.cpp voicesynth.h voicedata.h model.h
voicesynth.moc.cpp: voicesynth.h voicesynth.cpp voicedata.h 
	$(QT_BIN_DIR)/moc voicesynth.h -o voicesynth.moc.cpp
synth.o: synth.cpp synth.h model.h
synth.moc.o: synth.moc.cpp synth.h model.h
synth.moc.cpp: synth.h synth.cpp model.h
	$(QT_BIN_DIR)/moc synth.h -o synth.moc.cpp
voicedata.o: voicedata.cpp voicedata.h
model.o: model.cpp model.h voicedata.h
jackprocessor.o: jackprocessor.cpp jackprocessor.h model.h
jackprocessor.moc.o: jackprocessor.moc.cpp jackprocessor.h model.h
jackprocessor.moc.cpp: jackprocessor.h jackprocessor.cpp model.h
	$(QT_BIN_DIR)/moc jackprocessor.h -o jackprocessor.moc.cpp
main.o: main.cpp gui.h model.h
