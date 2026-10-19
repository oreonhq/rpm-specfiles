%global source0_hash ffef75b6bf16afbff399ccdc9ea5684226614aa6fecbd9696216bb0669453d0f
%global gh_commit    72a8f8e653710e18d83e5dd531eb5a71fc3223e6
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_branch    2.0-dev
%global gh_owner     composer
%global gh_project   composer
%global api_version  2.9.0
%global run_version  2.2.2
%global upstream_version 2.9.5
%global _phpunit       %{_bindir}/phpunit9
%global bashcompdir    %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)
%global bashcomproot   %(dirname %{bashcompdir} 2>/dev/null)
Name:           composer
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_lower}}
Release:        1%{?dist}
Summary:        Dependency Manager for PHP
License:        MIT
URL:            https://getcomposer.org/
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        %{name}-bash-completion
Source3:        %{name}.sh
Source4:        %{name}.csh
Source5:        makesrc.sh
Patch0:         %{name}-rpm.patch
Patch1:         %{name}-noxdg.patch
BuildArch:      noarch
Requires:       php(language)                           >= 7.2.5
Requires:       php-json
Requires:       php-cli
Requires:       /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
Requires:       php-curl
Requires:       php-openssl
Requires:       php-zip
Requires:       php-zlib
Requires:       php-ctype
Requires:       php-date
Requires:       php-dom
Requires:       php-filter
Requires:       php-hash
Requires:       php-iconv
Requires:       php-intl
Requires:       php-libxml
Requires:       php-mbstring
Requires:       php-pcntl
Requires:       php-pcre
Requires:       php-phar
Requires:       php-posix
Requires:       php-reflection
Requires:       php-spl
Requires:       php-tokenizer
Requires:       php-xsl
Requires:       php-zlib
Provides:       php-composer(composer-plugin-api) = %{api_version}
Provides:       php-composer(composer-runtime-api) = %{run_version}
Supplements:    php-pear
# oreon:deps
BuildRequires:  composer-generators
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-json
BuildRequires:  pkgconfig(bash-completion)
# /oreon:deps
%description
Composer helps you declare, manage and install dependencies of PHP projects,
ensuring you have the right stack everywhere.

Documentation: https://getcomposer.org/doc/

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p1 -b .rpm
%patch -P1 -p1 -b .noxdg
find . \( -name \*.rpm -o -name \*noxdg \) -delete -print

rm vendor/composer/ca-bundle/res/cacert.pem

: fix reported version
sed -e '/BRANCH_ALIAS_VERSION/s/@package_branch_alias_version@//' \
    -i src/Composer/Composer.php

: check Plugin API version
php -r '
namespace Composer;
include "src/bootstrap.php";
if (version_compare(Plugin\PluginInterface::PLUGIN_API_VERSION, "%{api_version}")) {
  printf("Plugin API version is %s, expected %s\n", Plugin\PluginInterface::PLUGIN_API_VERSION, "%{api_version}");
  exit(1);
}
if (version_compare(Composer::RUNTIME_API_VERSION, "%{run_version}")) {
  printf("Runtime API version is %s, expected %s\n", Composer::RUNTIME_API_VERSION, "%{run_version}");
  exit(1);
}'

%build

: Nothing to build
%install
: Profile scripts
install -Dpm 644 %{SOURCE1} %{buildroot}%{bashcompdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 644 %{SOURCE3} %{SOURCE4} %{buildroot}%{_sysconfdir}/profile.d/
: Library autoloader for compatibility
mkdir -p     %{buildroot}%{_datadir}/php/Composer
ln -s ../../composer/vendor/autoload.php %{buildroot}%{_datadir}/php/Composer/autoload.php
: Sources
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr src res vendor LICENSE\
         %{buildroot}%{_datadir}/%{name}/
: Command
install -Dpm 755 bin/%{name} %{buildroot}%{_bindir}/%{name}
: Licenses
ln -sf ../../%{name}/LICENSE LICENSE
cd vendor
for lic in */*/LICENSE
do dir=$(dirname $lic)
   own=$(dirname $dir)
   prj=$(basename $dir)
   ln -sf ../../composer/vendor/$own/$prj/LICENSE ../$own-$prj-LICENSE
done
%oreon_autofiles main

%check

: Check autoloader
php -r '
  include "%{buildroot}%{_datadir}/%{name}/src/bootstrap.php";
  exit (class_exists("Composer\\Composer") ? 0 : 1);
'
: Check compatibility autoloader
php -r '
  include "%{buildroot}%{_datadir}/php/Composer/autoload.php";
  exit (class_exists("Composer\\Composer") ? 0 : 2);
'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
