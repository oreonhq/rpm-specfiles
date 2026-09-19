%global source0_hash 9755933554235359435f1b0963a24c173df5d1b9c89b72c84db53da088bd7166

Name:          crrcsim-addon-models
Version:       0.2.0
Release:       29%{?dist}
Summary:       Model-Airplane Flight Simulation Program addon models
# Automatically converted from old format: CC-BY - review is highly recommended.
License:       LicenseRef-Callaway-CC-BY
URL:           http://sourceforge.net/apps/mediawiki/crrcsim/
Source0:       http://prdownloads.sourceforge.net/crrcsim/%{name}/%{name}-%{version}.zip
Source1:       http://creativecommons.org/licenses/by/3.0/legalcode.txt
Source2:       crrcsim-addon-models-license-question-arthur.eml
Source3:       crrcsim-addon-models-license-question-jan.eml
Requires:      crrcsim >= 0.9.5
BuildArch:     noarch

%description
Addon models for Crrcsim

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qcn %{name}-%{version}

# Correct EOL (preserve timestamps).
for i in \
    Readmefirst_Ellipse.txt \
    Readmefirst_Nyx.txt \
    Readmefirst_Europhia2k.txt \
    Readmefirst_Fireworks3.txt \
    Readmefirst_Skorpion.txt \
    Readmefirst_Freestyler.txt \
    Readmefirst_Crossfire.txt \
    install-cam.txt \
    Readmefirst_Erwin.txt; do
        sed 's#\r##g' documentation/$i > documentation/$i.tmp && \
        touch -r documentation/$i documentation/$i.tmp && \
        mv documentation/$i.tmp documentation/$i
done

%build

%install
mkdir -p %{buildroot}/%{_datadir}/crrcsim/

# Remove duplicates and older versions
rm documentation/Readmefirst_Crossfire.txt

rm models/Crossfire.xml \
   models/Erwin.xml \
   models/PilatusB4.xml \
   models/supra.xml

rm objects/Crossfire.ac \
   objects/Erwin.ac \
   objects/Fireworks_C.ac \
   objects/supra.ac

rm textures/CrossfireTexture.rgb \
   textures/Erwin.rgb \
   textures/Fireworks2.rgb \
   textures/PilB4Texture.rgb \
   textures/supra_texture_256.rgb

cp -ar models objects textures %{buildroot}/%{_datadir}/crrcsim
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%files
%doc documentation/*.txt legalcode.txt *.eml
%{_datadir}/crrcsim/models/*.xml
%{_datadir}/crrcsim/objects/*.ac
# Already exists in crrcsim-v0.9.13
%exclude %{_datadir}/crrcsim/objects/PilatusB4.ac
%{_datadir}/crrcsim/textures/*.rgb

%changelog
%autochangelog
