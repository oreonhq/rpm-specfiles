%global source0_hash f8625088f46d7448afaf014e30f2e6a634ea76930612f70a22352848f1c88c24

# Linked to the version of mediawiki in each Fedora release.
# Rawhide has 1.34, so we package the latest commit in the REL_1_34 branch.
# For non rawhide releases, this will change accordingly
# Remember to ensure that the upgrade path is maintained
%global commit be28231ebcd539fc99775811e5dc6df9064cfa94

%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global reponame mediawiki-extensions-LastModified

Name:           mediawiki-lastmodified
Version:        0
Release:        0.18.20200627git%{commit}%{?dist}
Summary:        Show the last modified page time

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.mediawiki.org/wiki/Extension:LastModified
Source0:        https://github.com/wikimedia/%{reponame}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch

Requires:       mediawiki >= 1.34

%description
The LastModified extension displays text on the page showing the last modified
page time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{reponame}-%{commit}
# Remove unneeded dotfiles
rm ./{.gitignore,.gitreview,.jshintrc} -v

%build
# Nothing here

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/{i18n,modules}
install -cpm 644 ./LastModified.php $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/
install -cpm 644 ./i18n/* $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/i18n/
install -cpm 644 ./modules/* $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/i18n/
install -cpm 644 ./*js $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/
install -cpm 644 ./*json $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/
install -cpm 644 ./*md $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/

%files
%{_datadir}/mediawiki/extensions/LastModified

%changelog
%autochangelog
