%global source0_hash eed973a236d624de60b429f11a6e0f430c516da3f53d94d3f5c569a662870405

# spec file for php-iamcal-lib-autolink
#
# Copyright (c) 2016-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    6a9e44d17f836806301b40723af673971a1a5112
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     iamcal
%global gh_project   lib_autolink
%global with_tests   0%{!?_without_tests:1}

Name:           php-iamcal-lib-autolink
Version:        1.9
Release:        7%{?dist}
Summary:        Adds anchors to urls in a text

Group:          Development/Libraries
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Used to retrieve a git snapshot with test suite
Source1:        makesrc.sh

BuildArch:      noarch
# For tests
%if %{with_tests}
BuildRequires:  php-cli
BuildRequires:  php-pcre
%endif

# From composer.json, nothing
# From phpcompatinfo report for 1.7
Requires:       php-pcre

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}

%description
Find URLs in HTML that are not already links, and make them into links.

Autoloader: %{_datadir}/php/%{name}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
: Nothing

%install
: Single file, only functions
install -Dpm 0644 lib_autolink.php %{buildroot}%{_datadir}/php/%{name}/lib_autolink.php

# from composer.json, "autoload": {
#    "files": ["lib_autolink.php"]
ln -s lib_autolink.php %{buildroot}%{_datadir}/php/%{name}/autoload.php

%check
%if %{with_tests}
sed -e 's/\$this/$thiz/' -i t/testmore.php

>tests.log
for cmd in php php80 php81 php82 php83; do
  if which $cmd; then
    for unit in t/*.t; do
      $cmd $unit | tee -a tests.log
    done
  fi
done

grep '^not ok' tests.log && exit 1 || exit 0
%else
: Test suite disabled
%endif

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{name}

%changelog
%autochangelog
