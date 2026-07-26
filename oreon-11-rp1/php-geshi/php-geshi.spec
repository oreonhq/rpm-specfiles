%global source0_hash 553d439c543ff4157fed59c3a5c9f5730371ae6c02a08aa89d1b9aebceb3f63f

Name:           php-geshi
Summary:        Generic syntax highlighter
License:        GPL-2.0-or-later

%global git_commit 7884d22244c6d2de5ac7ffd919ce4add02b36e66
%global git_date 20230219
%global git_short %(c="%{git_commit}"; echo "${c:0:7}")

Version:        1.0.9.1
Release:        20.%{git_date}git%{git_short}%{?dist}

URL:            https://github.com/GeSHi/geshi-1.0
Source0:        %{url}/archive/%{git_commit}/GeSHi-%{git_commit}.tar.gz

# Some of the project files do not pass tests, fix those
Patch1:         0001-fix-LangCheckTest-failures.patch

BuildArch:      noarch

%if 0%{?fedora}
BuildRequires:  phpunit8
%endif
BuildRequires:  php-mbstring
BuildRequires:  php-pcre

Requires:       php-mbstring
Requires:       php-pcre

Provides:       php-composer(geshi/geshi) = %{version}

%description
GeSHi aims to be a simple but powerful highlighting class,
with the following goals:
    * Support for a wide range of popular languages
    * Easy to add a new language for highlighting
    * Highly customisable output formats

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n geshi-1.0-%{git_commit}

find docs -type f -exec chmod a-x {} ';'
find . -type f -name "*.php" -exec chmod a-x {} ';'

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/php/
cd src
cp -a geshi geshi.php %{buildroot}%{_datadir}/php/

%check
%if 0%{?fedora}
phpunit8 --verbose
%endif

%files
%license LICENSE
%doc BUGS CHANGELOG README.md THANKS
%doc docs/* contrib/
%doc composer.json
%{_datadir}/php/geshi.php
%{_datadir}/php/geshi/

%changelog
%autochangelog
