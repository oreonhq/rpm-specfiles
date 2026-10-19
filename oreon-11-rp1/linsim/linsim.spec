%global source0_hash 84d3efd0f655a754172716d2379b7b23b44f04d2183382eb9aa4829e1a06f735
Name:           linsim
Version:        2.0.4
Release:        12%{?dist}
Summary:        Tool for Amateur Radio Digital Mode evaluation
License:        GPL-3.0-or-later
URL:            http://www.w1hkj.com
Source0:        http://www.w1hkj.com/files/test_suite/%{name}-%{version}.tar.gz
Source99:       linsim.appdata.xml
Patch0:         linsim-desktop.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  libXft-devel
BuildRequires:  libappstream-glib
BuildRequires:  libpng-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  make
# /oreon:deps
%description
Linsim is designed to read and then add path simulation to any monophonic wav
file recorded at any sampling rate. It works particularly well with files that
were created using fldigi’s audio capture and audio generate functions. The
entire wav file will be saved to computer memory and then duplicated during the
signal processing. The user should try to keep the length of the wav file at 20
Mg or less, but the author has tested some 200 Mg files on both Linux and
Windows-8 without causing a program fault. These files were original VOAR
broadcasts of about 30 minutes duration. The objective of this type of
simulation is to finally measure the character error rate (CER) and bit error
rate (BER) of a specific modem type and decoder design. For most modems a
sequence of 1000 characters provides a sufficient level of confidence in the
CER measurment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export LIBS="-lfltk"
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
