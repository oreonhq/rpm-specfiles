%global source0_hash 39118655f8fc0d5554a3c45a851c8256169b51ed8a5c157fdb8ae3fc6212a2c9
%bcond_without tests
%undefine __brp_mangle_shebangs
%global gh_commit    f3683aa0db2e8e09287c2bb33a595b2873ea9176
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpcpd
%global php_home     %{_datadir}/php
%global pk_vendor    sebastian
%global pk_project   phpcpd
%global ns_vendor    SebastianBergmann
%global ns_project   PHPCPD
Name:           %{pk_project}
Version:        6.0.3
Release:        1%{?dist}
Summary:        Copy/Paste Detector (CPD) for PHP code
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
Patch0:         %{gh_project}-rpm.patch
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 7.3
Requires:       php-dom
Requires:       (php-composer(sebastian/cli-parser)      >= 1.0   with php-composer(sebastian/cli-parser)      < 2)
Requires:       (php-composer(sebastian/version)         >= 3.0   with php-composer(sebastian/version)         < 4)
Requires:       (php-composer(phpunit/php-file-iterator) >= 3.0   with php-composer(phpunit/php-file-iterator) < 4)
Requires:       (php-composer(phpunit/php-timer)         >= 5.0   with php-composer(phpunit/php-timer)         < 6)
Requires:       php-cli
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl
Requires:       php-tokenizer
Requires:       php-xml
Obsoletes:      php-phpunit-%{pk_project} < 4
Provides:       php-phpunit-%{pk_project} = %{version}
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 3.0 with php-composer(phpunit/php-file-iterator) < 4)
BuildRequires:  (php-composer(phpunit/php-timer) >= 5.0 with php-composer(phpunit/php-timer) < 6)
BuildRequires:  (php-composer(sebastian/cli-parser) >= 1.0 with php-composer(sebastian/cli-parser) < 2)
BuildRequires:  (php-composer(sebastian/version) >= 3.0 with php-composer(sebastian/version) < 4)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit9
# /oreon:deps
%description
phpcpd is a Copy/Paste Detector (CPD) for PHP code.

The goal of phpcpd is not not to replace more sophisticated tools such as phpcs,
pdepend, or phpmd, but rather to provide an alternative to them when you just
need to get a quick overview of duplicated code in a project.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p1 -b .rpm

%build

phpab \
  --output   src/autoload.php \
  --template fedora \
  src
cat << 'EOF' | tee -a src/autoload.php
// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{ns_vendor}/CliParser/autoload.php',
    '%{php_home}/%{ns_vendor}/FileIterator3/autoload.php',
    '%{php_home}/%{ns_vendor}/Timer5/autoload.php',
    '%{php_home}/%{ns_vendor}/Version3/autoload.php',
]);
EOF
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}
install -D -p -m 755 phpcpd %{buildroot}%{_bindir}/phpcpd
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
ln -s %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php vendor/autoload.php
ret=0;
for cmd in php php73 php74 php80; do
   if which $cmd; then
      $cmd %{_bindir}/phpunit9 --verbose || ret=1
   fi
done
exit $ret
%else
: Test suite skipped
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
