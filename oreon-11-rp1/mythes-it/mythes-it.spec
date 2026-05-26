# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 ed840e5e90fa7752761edc5729a5c5bcb66caa3cc31fcd738235d235160ccc88
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:         mythes-it
Summary:      Italian thesaurus
Version:      5.1.1
Release:      %autorelease
# The license text is embedded within the README files
# Here we specify the thesaurus license only as other files are not packaged 
License:      GPL-3.0-only
URL:          https://pagure.io/dizionario_italiano
Source:        https://pagure.io/dizionario_italiano/archive/5.1.1/dizionario_italiano-5.1.1.tar.gz

BuildArch:    noarch
Requires:     mythes
Supplements:  (mythes and langpacks-it)

%description
Italian thesaurus.


%prep
%oreon_verify_sources
%autosetup -n dizionario_italiano-%{version}


%build
# Nothing to do


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_it_IT_v2.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_it_IT_v2.dat
cp -p th_it_IT_v2.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_it_IT_v2.idx

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
it_IT_aliases="it_CH"
for lang in $it_IT_aliases; do
        ln -s th_it_IT_v2.dat "th_"$lang"_v2.dat"
        ln -s th_it_IT_v2.idx "th_"$lang"_v2.idx"
done


%files
%license LICENSES/gpl-3.0.txt
%doc CHANGELOG.txt README.md README_th_it_IT.txt
%{_datadir}/mythes/th_it_IT_v2.*
%{_datadir}/mythes/th_it_CH_v2.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.1-1
- Prepare for Oreon 11 (RP1)
