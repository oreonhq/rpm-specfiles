%global source0_hash 8ef3179199850b9d6afbb2939e1aa0b8b8372b1d5b51b8df018c8f518a5b9b67

%global author   splitbrain
%global project  php-jsstrip
Name: php-%{author}-%{project}

Version: 1.0.1
Release: 9%{?dist}

Summary: PHP-based JavaScript compressor
License: BSD-3-Clause

URL: https://github.com/%{author}/%{project}

# Upstream explicitly marked phpunit.xml and the tests/ directory
# as "export-ignore" in their .gitattributes file, which makes
# GitHub skip those files when generating tarballs. But we *do* want
# those files, since we *do* want to run the tests.
#
# The php-jsstrip-get-source.sh script is used to perform a git clone
# of the reposistory (which does contain said files) and zip it up.
Source0: %{project}-%{version}.tar.gz
Source99: %{project}-get-source.sh

BuildArch: noarch

%global with_tests 1

BuildRequires: php(language) >= 7.2.0
BuildRequires: php-fedora-autoloader-devel

%if 0%{?with_tests}
BuildRequires: phpunit8
%endif

Requires: php(language) >= 7.2.0

Requires: php-composer(fedora/autoloader)

Provides: php-composer(%{author}/%{project}) = %{version}

# Use a PSR-0 compatible directory hierarchy
%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global pkgauthordir %{phpdir}/%{author}
%global pkgdir %{pkgauthordir}/JSStrip

%description
PHP JSStrip is PHP port of the original Python tool, jsstrip.py. It was
originally ported to PHP in 2006 as part of the DokuWiki wiki engine.
It has received several improvements over the years and is now available as a
standalone library.

Quoting the original description: jsstrip is a open-source library to remove
whitespace and comments from a JavaScript file. You might want to do this to
optimize size and performance, or to make a file harder to read. It typically
makes 30-40% savings in file size.

WARNING: jsstrip is not a true JavaScript parser. It assumes you have properly
delimited the 'end of line' using a ';' (semicolon). ALWAYS test the stripped
version before deploying to production.

Autoloader: %{pkgdir}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{project}-%{version}

%build
# Create autoloader
phpab \
	--template fedora \
	--output autoload.php \
	--basedir src/ \
	./composer.json
cat autoload.php

%install
install -d -m 755 %{buildroot}%{pkgauthordir}
cp -a src %{buildroot}%{pkgdir}

cp autoload.php %{buildroot}%{pkgdir}/autoload.php

%if 0%{?with_tests}
%check
phpunit8 --verbose --bootstrap %{buildroot}%{pkgdir}/autoload.php
%endif

%files
%license LICENSE
%doc composer.json
%doc README.md
%{pkgauthordir}/

%changelog
%autochangelog
