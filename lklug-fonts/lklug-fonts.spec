BuildRequires: fontforge
BuildRequires: make

# Do not trust font metadata versionning unless you've checked upstream does
# update versions on file changes. When in doubt use the timestamp of the most
# recent file as version.
%global cvsdate 20090803
Version: 0.6
Release: 36.%{cvsdate}cvs%{?dist}
URL:    http://sinhala.sourceforge.net/

%global fontlicense       GPL-2.0-only
%global fontlicenses      COPYING 
%global fontdocs          CREDITS README.fonts                            
            
%global fontfamily        lklug
%global fontsummary       Fonts for Sinhala language
%global fonts             *.ttf
%global fontconfs         %{SOURCE1}  

%global fontdescription   %{expand:
The lklug-fonts package contains fonts for the display of
Sinhala. The original font for TeX/LaTeX is developed by Yannis
Haralambous and are in GPL. OTF tables are added by Anuradha
Ratnaweera and Harshani Devadithya.
}

# cvs snapshot created with following steps
#cvs -z3 -d:pserver:anonymous@sinhala.cvs.sourceforge.net:/cvsroot/sinhala co -P sinhala/fonts
#cd sinhala/fonts/
#tar -czf lklug-%%{cvsdate}.tar.gz convert.ff COPYING  CREDITS lklug.sfd Makefile README.fonts
Source: lklug-%{cvsdate}.tar.gz
Source1: 65-%{fontpkgname}.conf

%fontpkg

%prep
%autosetup -c

%build
make
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6-36.
- Prepare for Oreon 11 (RP1)
