%global source0_hash 42d18929af4cbdd13784a51c509175d4458010332d238310b4d4cd962e2bc1db

%global tag         bravura-%{version}
%global date        20210209
%global forgeurl    https://github.com/steinbergmedia/bravura

Version:        1.392
URL:            https://www.smufl.org/fonts/
VCS:            git:%{forgeurl}.git

%forgemeta

Release:        12%{?dist}

%global foundry          steinberg
%global fontorg          org.smufl
%global fontlicense      OFL-1.1-RFN
%global fontlicenses     LICENSE.txt
%global fontdocs         README.md redist/bravura-text.md redist/FONTLOG.txt
%global fontdocsex       %{fontlicenses}

%global common_description %{expand:Bravura is an OpenType music font developed for Steinberg's Dorico music
notation and composition software.  It is also the reference font for Standard
Music Font Layout (SMuFL), which provides a standard way of mapping the
thousands of musical symbols required by conventional music notation into the
Private Use Area in Unicode's Basic Multilingual Plane for a single
(format-independent) font.}

%global fontfamily0      Bravura
%global fontsummary0     Bravura music font
%global fonts0           redist/otf/Bravura.otf
%global fontconfs0       %{SOURCE1}
%global fontdescription0 %{expand:%{common_description}

This package contains the Bravura font family.  It is a Unicode typeface
designed by Steinberg for its music notation and scoring application.}

%global fontfamily1      BravuraText
%global fontsummary1     Bravura text font
%global fonts1           redist/otf/BravuraText.otf
%global fontconfs1       %{SOURCE2}
%global fontdescription1 %{expand:%{common_description}

This package contains the Bravura Text font family.  It is a Unicode typeface
designed by Steinberg for its music notation and scoring application.}

Source0:        %{forgesource}
Source1:        65-%{fontpkgname0}.conf
Source2:        65-%{fontpkgname1}.conf

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%fontpkg -a
%fontmetapkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup
 
%build
%fontbuild -a

%install
%fontinstall -a

# Install the SMuFL metadata
mkdir -p %{buildroot}%{_datadir}/SMuFL/Fonts/Bravura
install -m 0644 -p redist/bravura_metadata.json \
        %{buildroot}%{_datadir}/SMuFL/Fonts/Bravura/metadata.json
ln -s metadata.json %{buildroot}%{_datadir}/SMuFL/Fonts/Bravura/Bravura.json

%check
%fontcheck -a

%fontfiles -z 0
%{_datadir}/SMuFL/

%fontfiles -z 1

%changelog
%autochangelog
