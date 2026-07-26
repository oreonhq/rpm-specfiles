%global source0_hash 0a7b1548ecceb249992eb0042d443536a7396bee080893f38518c147a63c9f35

# The Scripts font has a different version from the other two
%global petalumaver       1.065
%global petalumascriptver 1.10
%global tag               petaluma-%{version}
%global date              20210127
%global forgeurl          https://github.com/steinbergmedia/petaluma

Version:        %{petalumaver}
URL:            https://www.smufl.org/fonts/
VCS:            git:%{forgeurl}.git

%forgemeta

# If both %%petalumaver and %%petalumascriptver were increased,
# release should be reset to 1. Otherwise, keep increasing it so that
# name-version-release keeps growing for both subpackages.
Release:        14%{?dist}

%global foundry          steinberg
%global fontorg          org.smufl
%global fontlicense      OFL-1.1-RFN
%global fontlicenses     redist/OFL*.txt
%global fontdocs         README.md redist/FONTLOG.txt
%global fontdocsex       %{fontlicenses}

%global common_description %{expand:Petaluma is a Unicode typeface designed by Steinberg for its Dorico music
notation and scoring application.  It is compliant with version 1.3 of the
Standard Music Font Layout (SMuFL), a community-driven standard for how music
symbols should be laid out in the Unicode Private Use Area (PUA) in the Basic
Multilingual Plane (BMP) for compatibility between different scoring
applications.}

%global fontfamily0      Petaluma
%global fontsummary0     Petaluma music font
%global fonts0           redist/otf/Petaluma.otf
%global fontconfs0       %{SOURCE1}
%global fontdescription0 %{expand:%{common_description}

This package contains the Petaluma font.  It is a Unicode typeface designed by
Steinberg for its music notation and scoring application.}

%global fontfamily1      PetalumaText
%global fontsummary1     Petaluma text font
%global fonts1           redist/otf/PetalumaText.otf
%global fontconfs1       %{SOURCE2}
%global fontdescription1 %{expand:%{common_description}

This package contains the Petaluma Text font.  It is a Unicode typeface
designed by Steinberg for its music notation and scoring application.}

%global fontfamily2      PetalumaScript
%global fontsummary2     Petaluma script font
%global fonts2           redist/otf/PetalumaScript.otf
%global fontconfs2       %{SOURCE3}
%global fontdescription2 %{expand:%{common_description}
%global fontpkgheader2   %{expand:
Version:        %{petalumascriptver}
}

This package contains the Petaluma Script font.  It is a Unicode typeface
designed by Steinberg for its music notation and scoring application.}

Source0:        %{forgesource}
Source1:        65-%{fontpkgname0}.conf
Source2:        65-%{fontpkgname1}.conf
Source3:        65-%{fontpkgname2}.conf

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%fontpkg -a

# We cannot use %%fontmetapkg, because it doesn't know how to deal with a
# different version number for the Scripts font.
%package        all
Summary:        All the font packages generated from %{name}
Version:        %{petalumaver}
Requires:       %{name} = %{petalumaver}-%{release}
Requires:       steinberg-petalumatext-fonts = %{petalumaver}-%{release}
Requires:       steinberg-petalumascript-fonts = %{petalumascriptver}-%{release}

%description    all
This meta-package installs all the font packages generated from the
%{name} source package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build
%fontbuild -a

%install
%fontinstall -a

# Install the SMuFL metadata
mkdir -p %{buildroot}%{_datadir}/SMuFL/Fonts/Petaluma
install -m 0644 -p redist/petaluma_metadata.json \
        %{buildroot}%{_datadir}/SMuFL/Fonts/Petaluma/metadata.json
ln -s metadata.json %{buildroot}%{_datadir}/SMuFL/Fonts/Petaluma/Petaluma.json

%check
%fontcheck -a

%fontfiles -z 0
%{_datadir}/SMuFL/

%fontfiles -z 1

%fontfiles -z 2

%files          all

%changelog
%autochangelog
