%global source0_hash 3a3587c0a524c17d0dad9673a160b90cd776e836838474e173b549ed864352ee

%global pie_vend   imagick
%global pie_proj   imagick
%global pecl_name  imagick
%global ini_name   40-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}

Summary:        Provides a wrapper to the ImageMagick library
Name:           php-pecl-%pecl_name
Version:        3.8.1
Release:        2%{?dist}
License:        PHP-3.01
URL:            https://pecl.php.net/package/%pecl_name

Source0:        https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:    %{ix86}

BuildRequires:  php-pear
BuildRequires:  php-devel
BuildRequires:  pkgconfig(ImageMagick)

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

# Extension
Provides:       php-%pecl_name                   = %{version}
Provides:       php-%pecl_name%{?_isa}           = %{version}
# PECL
Provides:       php-pecl(%pecl_name)             = %{version}
Provides:       php-pecl(%pecl_name)%{?_isa}     = %{version}
# PIE
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj}      = %{version}

Conflicts:      php-pecl-gmagick

%description
Imagick is a native php extension to create and modify images using the
ImageMagick API.

%package devel
Summary:       %{pecl_name} extension developer files (header)
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      php-devel%{?_isa}

%description devel
These are the files needed to compile programs using %{pecl_name} extension.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

# don't install any font (and test using it)
# don't install empty file (d41d8cd98f00b204e9800998ecf8427e)
sed -e '/anonymous_pro_minus.ttf/d' \
    -e '/015-imagickdrawsetresolution.phpt/d' \
    -e '/OFL.txt/d' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

if grep '\.ttf' package.xml
then : "Font files detected!"
     exit 1
fi

cd %{sources}
: Avoid arginfo to be regenerated
rm *.stub.php

extver=$(sed -n '/#define PHP_IMAGICK_VERSION/{s/.* "//;s/".*$//;p}' php_imagick.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream version is ${extver}, expecting %{version}%{?prever}.
   exit 1
fi
cd ..

cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension = %{pecl_name}.so

; Documentation: http://php.net/imagick

; Don't check builtime and runtime versions of ImageMagick
imagick.skip_version_check=1

; Fixes a drawing bug with locales that use ',' as float separators.
;imagick.locale_fix=0

; Used to enable the image progress monitor.
;imagick.progress_monitor=0

; multi-thread management
;imagick.set_single_thread => 1 => 1
;imagick.shutdown_sleep_count => 10 => 10

; to allow null images
;imagick.allow_zero_dimension_images => 0 => 0
EOF

%build
cd %{sources}

: Standard build
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure --with-imagick=%{prefix} --with-php-config=%{__phpconfig}

%make_build

%install
cd %{sources}
: Install the extension
%make_install

: Drop in the bit of configuration
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -p -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install Test and Documentation
for i in $(grep 'role="test"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do [ -f $i ] && install -Dpm 644 $i %{buildroot}%{pecl_testdir}/%{pecl_name}/$i
done
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do [ -f $i ] && install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
cd %{sources}

: simple module load test for the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

# Ignore know failed test on some ach (s390x, armv7hl, aarch64) with timeout
rm tests/229_Tutorial_fxAnalyzeImage_case1.phpt
rm tests/244_Tutorial_psychedelicFontGif_basic.phpt
# very long, and erratic results
rm tests/073_Imagick_forwardFourierTransformImage_basic.phpt
rm tests/086_Imagick_forwardFourierTransformImage_basic.phpt
rm tests/151_Imagick_subImageMatch_basic.phpt
rm tests/316_Imagick_getImageKurtosis.phpt
# change in 7.1.2
# see https://github.com/Imagick/imagick/issues/737
rm tests/024-ispixelsimilar.phpt

: upstream test suite for the extension
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff %{?_smp_mflags}

%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%files devel
%doc %{pecl_testdir}/%{pecl_name}
%{php_incldir}/ext/%{pecl_name}

%changelog
%autochangelog
