%global source0_hash 672c3487883ec1ef83d9254240d4327b014212abc823d06d15816095867315e1

BuildArch: noarch

Version:        1.31.0
Release:        23%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
#URL:            

Source0:        http://gsdview.appspot.com/chromeos-localmirror/distfiles/%{archivename}.tar.bz2
Source1:        62-%{fontpkgname1}.conf
Source2:        62-%{fontpkgname2}.conf
Source3:        62-%{fontpkgname3}.conf
Source4:        30-0-%{fontpkgname1}.conf
Source5:        30-0-%{fontpkgname2}.conf
Source6:        30-0-%{fontpkgname3}.conf
# Upstream has not provided license text in their tarball release
# Add ASL2.0 license text in LICENSE-2.0.txt file
Source8:        LICENSE-2.0.txt

%global foundry           google
%global fontlicense       Apache-2.0
%global fontlicenses      LICENSE-2.0.txt

%global common_description %{expand:
This package contains a collections of fonts that offers improved on-screen
readability characteristics and the pan-European WGL character set and solves
the needs of developers looking for width-compatible fonts to address document
portability across platforms.}

%global fontsummary The width-compatible fonts for improved on-screen readability

%global archivename croscorefonts-%{version}

%global fontfamily1       Arimo
%global fontsummary1      The croscore Arimo family fonts
%global fontpkgheader1    %{expand:
Provides:  google-croscore-arimo-fonts = %{version}-%{release}
Obsoletes: google-croscore-arimo-fonts < %{version}-%{release}
}
%global fonts1            Arimo*.ttf
%global fontconfs1        %{SOURCE1} %{SOURCE4}
%global fontdescription1  %{expand:
%{common_description}

Arimo was designed by Steve Matteson as an innovative, refreshing sans serif
design that is metrically compatible with Arial. Arimo offers improved 
on-screen readability characteristics and the pan-European WGL character set 
and solves the needs of developers looking for width-compatible fonts to 
address document portability across platforms.}

%global fontfamily2       Cousine
%global fontsummary2      The croscore Cousine family fonts
%global fontpkgheader2    %{expand:
Provides:  google-croscore-cousine-fonts = %{version}-%{release}
Obsoletes: google-croscore-cousine-fonts < %{version}-%{release}
}
%global fonts2            Cousine*.ttf
%global fontconfs2        %{SOURCE2} %{SOURCE5}
%global fontdescription2  %{expand:
%{common_description}

Cousine was designed by Steve Matteson as an innovative, refreshing sans serif
design that is metrically compatible with Courier New. Cousine offers improved
on-screen readability characteristics and the pan-European WGL character set
and solves the needs of developers looking for width-compatible fonts to 
address document portability across platforms.}

%global fontfamily3       Tinos
%global fontsummary3      The croscore Tinos family fonts
%global fontpkgheader3    %{expand:
Provides:  google-croscore-tinos-fonts = %{version}-%{release}
Obsoletes: google-croscore-tinos-fonts < %{version}-%{release}
}
%global fonts3            Tinos*.ttf
%global fontconfs3        %{SOURCE3} %{SOURCE6}
%global fontdescription3  %{expand:
%{common_description}

Tinos was designed by Steve Matteson as an innovative, refreshing serif design
that is metrically compatible with Times New Roman. Tinos offers improved
on-screen readability characteristics and the pan-European WGL character set
and solves the needs of developers looking for width-compatible fonts to
address document portability across platforms.}

Name: google-croscore-fonts
Summary: The width-compatible fonts for improved on-screen readability

%description
%wordwrap -v common_description

%fontpkg -a

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n croscorefonts-%{version}
cp -p %{SOURCE8} .

%build
%fontbuild -a

%install
echo %{fontpkgname}
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
