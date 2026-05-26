Name:           hyphen-it
Summary:        Italian hyphenation rules
Version:        5.1.1
Release:        %autorelease
# The license text is embedded within the README files
# Here we specify the thesaurus license only as other files are not packaged 
License:        LGPL-2.1-only
URL:            https://pagure.io/dizionario_italiano
Source:        https://pagure.io/dizionario_italiano/archive/5.1.1/dizionario_italiano-5.1.1.tar.gz
# oreon url source checksums begin
%global source0_sha256 ed840e5e90fa7752761edc5729a5c5bcb66caa3cc31fcd738235d235160ccc88
%global source0_file dizionario_italiano-5.1.1.tar.gz
# oreon url source checksums end

BuildArch:      noarch
Requires:       hyphen
Supplements:    (hyphen and langpacks-it)
Provides:       hyphen-la = %{version}

%description
Italian hyphenation rules.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/dizionario_italiano-5.1.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ed840e5e90fa7752761edc5729a5c5bcb66caa3cc31fcd738235d235160ccc88" || { echo "oreon: Source0 SHA256 mismatch for dizionario_italiano-5.1.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n dizionario_italiano-%{version}


%build
# Nothing to do


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_it_IT.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
#http://extensions.services.openoffice.org/project/dict-la uses the it_IT for Latin
#so we'll do the same
it_IT_aliases="it_CH la_VA"
for lang in $it_IT_aliases; do
        ln -s hyph_it_IT.dic "hyph_"$lang".dic"
done


%files
%license LICENSES/lgpl-2.1.txt
%doc CHANGELOG.txt README.md README_hyph_it_IT.txt
%{_datadir}/hyphen/hyph_it_IT.dic
%{_datadir}/hyphen/hyph_it_CH.dic
%{_datadir}/hyphen/hyph_la_VA.dic


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.1-1
- Prepare for Oreon 11 (RP1)
