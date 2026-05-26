# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 4c3f92167f486e0f69f14c16a566f0b2acc09fff4d7e28f0848e17a95a677e68
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-te
Summary: Telugu hunspell dictionaries
Version: 1.0.0
Release: 28%{?dist}
Epoch:   1
##Upstream is unresponsive so unable to verify license version
License:        GPL-1.0-or-later
URL:            https://gitorious.org/hunspell_dictionaries/hunspell_dictionaries.git
Source0:        http://anishpatil.fedorapeople.org/te_in.%{version}.tar.gz
BuildArch:      noarch

Requires:       hunspell
Supplements: (hunspell and langpacks-te)

%description
Telugu hunspell dictionaries.

%prep
%oreon_verify_sources
%autosetup -c -n te_IN

%build


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p te_IN/*.dic te_IN/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files 
%license te_IN/COPYING te_IN/Copyright
%doc te_IN/README
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-28
- Prepare for Oreon 11 (RP1)
