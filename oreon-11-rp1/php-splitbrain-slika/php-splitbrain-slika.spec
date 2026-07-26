%global source0_hash 4e283e79733cc08ada31ac5baa032f3f3b8b1faada3ed558ca3ad80b278e84ab

%global author   splitbrain
%global project  slika
Name: php-%{author}-%{project}

Version: 1.0.7
Release: 5%{?dist}

Summary: Image handling library for PHP
License: MIT

URL: https://github.com/%{author}/%{project}

# The test cases work by editing some images and comparing the actual result
# to the expected one. The images are stored in Git-LFS and are not included
# in the code archives available on GitHub.
#
# The slika-get-archive.sh script is used to clone the repository,
# fetch the images and zip it all up.
Source0: %{project}-%{version}.zip
Source99: slika-get-archive.sh

BuildArch: noarch

%global with_tests 1

BuildRequires: php(language) >= 7.0.0
BuildRequires: php-fedora-autoloader-devel

%if 0%{with_tests}
BuildRequires: ImageMagick
BuildRequires: php-gd
BuildRequires: php-pcre
BuildRequires: phpunit8
%endif

Requires: php(language) >= 7.0.0
Requires: php-pcre

Requires: php-composer(fedora/autoloader)

Requires: (php-gd or ImageMagick)
Recommends: php-gd

Provides: php-composer(%{author}/%{project}) = %{version}

# Use a PSR-0 compatible directory hierarchy
%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global pkgauthordir %{phpdir}/%{author}
%global pkgdir %{pkgauthordir}/slika

%description
Slika is a simple image handling library for PHP. It covers only
the bare basics you need when handling images: resizing, cropping, rotation.

It can use either PHP's libGD or a locally installed ImageMagick binary.

Autoloader: %{pkgdir}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{project}-%{version}

# Exclude the tests from the composer file
sed -e '/"splitbrain\\\\slika\\\\tests\\\\":/d' -i composer.json

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

%if 0%{with_tests}
%check
cat > ./bootstrap.php <<EOF
<?php
require '%{buildroot}%{pkgdir}/autoload.php';

require __DIR__ . '/tests/TestCase.php';
EOF

phpunit8 --verbose --bootstrap ./bootstrap.php
%endif

%files
%license LICENSE
%doc composer.json
%doc README.md
%{pkgauthordir}/

%changelog
%autochangelog
