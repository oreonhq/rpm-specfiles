%global source0_hash f850b88cbb64529655514b7cfe01c56133e21929374b3e3b90813bc227eac789

%global sse_cxxflags %{optflags}
%global sse_cmakeflags -DHOST_SUPPORTS_SSE:BOOL=FALSE
%ifarch %{ix86}
%global with_sse %{!?_without_sse:1}%{?_without_sse:0}
%if %{with_sse}
%global sse_cxxflags -DSSE_OPTIMIZATIONS -DARCH_X86 %{optflags}
%global sse_cmakeflags -DHOST_SUPPORTS_SSE:BOOL=TRUE -DIS_ARCH_X86:BOOL=TRUE
%endif
%endif
%ifarch ia64 x86_64
%global with_sse 1
%global sse_cxxflags -DSSE_OPTIMIZATIONS -DUSE_XMMINTRIN -DARCH_X86 -DUSE_X86_64_ASM %{optflags}
%global sse_cmakeflags -DHOST_SUPPORTS_SSE:BOOL=TRUE -DIS_ARCH_X86_64:BOOL=TRUE
%endif

Name:           traverso
Version:        0.49.6
Release:        17%{?dist}
Summary:        Multitrack Audio Recording and Editing Suite

License:        GPL-2.0-or-later
URL:            http://traverso-daw.org/
Source0:        http://traverso-daw.org/%{name}-%{version}.tar.gz
# lower the rtprio requirement to 20, for compliance with our jack
Patch0:         %{name}-priority.patch
# Fix DSO linking
Patch1:         traverso-gcc49.patch
# Patch2:         gcc6-buildfix-01.patch

BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  flac-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  lame-devel
BuildRequires:  lilv-devel
BuildRequires:  libmad-devel
BuildRequires:  libogg-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libvorbis-devel
BuildRequires:  portaudio-devel
# Native pulseaudio is not supported yet.
#BuildRequires:  pulseaudio-libs-devel
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  raptor2-devel
BuildRequires:  redland-devel
BuildRequires:  wavpack-devel

# For directory ownership:
Requires:       hicolor-icon-theme
Requires:       shared-mime-info

%description
Traverso Digital Audio Workstation is a cross platform multitrack audio 
recording  and editing suite, with an innovative and easy to master User
Interface. It's suited for both the professional and home user, who needs a
robust and solid DAW. 

Traverso is a complete solution from recording to CD Mastering. By supplying
many common tools in one package, you don't have to learn how to use lots of
applications with different user interfaces. This considerably lowers the 
learning curve, letting you get your audio processing work done faster!

A unique approach to non-linear audio processing was developed for Traverso to
provide extremely solid and robust audio processing and editing. Adding and 
removal of effects plugins, moving Audio Clips and creating new Tracks during 
playback are all perfectly safe, giving you instant feedback on your work! 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix permission issues
chmod 644 ChangeLog TODO
for ext in h cpp; do
   find . -name "*.$ext" -exec chmod 644 {} \;
done

# To match the freedesktop standards
sed -i -e '\|^MimeType=.*[^;]$|s|$|;|' \
    resources/%{name}.desktop

# We use the system slv2, so just to make sure
rm -fr src/3rdparty/slv2

# For proper slv2 detection
sed -i 's|libslv2|slv2|g' CMakeLists.txt

%build
# Build the actual program
%{cmake}                                               \
         -DWANT_MP3_ENCODE=ON                          \
         -DDETECT_HOST_CPU_FEATURES=OFF                \
         -DWANT_PORTAUDIO=ON                           \
         -DCXX_FLAGS:STRING="%{sse_cxxflags}"          \
         %{sse_cmakeflags}                             \
         %{nil}
%cmake_build

# Add Comment to the .desktop file
echo "Comment=Digital Audio Workstation" >> resources/%{name}.desktop

%install
%cmake_install

# icons
install -dm 755 %{buildroot}%{_datadir}/icons/hicolor/
cp -a resources/freedesktop/icons/* %{buildroot}%{_datadir}/icons/hicolor/

# desktop file
install -dm 755 %{buildroot}%{_datadir}/applications/
desktop-file-install                          \
   --dir %{buildroot}%{_datadir}/applications \
   --remove-mime-type=text/plain              \
   --add-mime-type=application/x-traverso     \
   --add-category=X-Multitrack                \
   --add-category=Sequencer                   \
   --remove-key=Path                          \
   resources/%{name}.desktop

# mime-type file
install -dm 755 %{buildroot}%{_datadir}/mime/packages/
install -pm 644 resources/x-%{name}.xml %{buildroot}%{_datadir}/mime/packages/

%files
%license COPYING
%doc AUTHORS ChangeLog COPYRIGHT HISTORY README TODO
%doc resources/projectconversion/2_to_3.html resources/help.text
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/*.xml

%changelog
%autochangelog
