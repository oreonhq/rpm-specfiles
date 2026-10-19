%global source0_hash 6ff98b5b007410e7bace4c6771f4dd6a06effc0557cbad7742ae1505ed809bed
%bcond_without       tests
%global gh_commit    0525c73950de35ded110cffafb9892946d7771b5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      2025-11-10
%global gh_owner     PHPCSStandards
%global gh_project   PHP_CodeSniffer
%global pear_phpdir  %{_datadir}/pear
%global upstream_version 4.0.1
Name:           php-pear-PHP-CodeSniffer
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
Summary:        PHP coding standards enforcement tool
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
Patch0:         %{name}-rpm.patch
BuildArch:      noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit10
%endif
Requires:       php(language) >= 7.2
Requires:       php-tokenizer
Requires:       php-xmlwriter
Requires:       php-simplexml
Requires:       php-dom
Requires:       php-iconv
Requires:       php-intl
Provides:       php-pear(%{gh_project}) = %{version}
Provides:       php-composer(squizlabs/php_codesniffer) = %{version}
Provides:       phpcs = %{version}
Obsoletes:      phpcs < %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-bcmath
BuildRequires:  php-dom
BuildRequires:  php-iconv
BuildRequires:  php-intl
BuildRequires:  php-simplexml
BuildRequires:  php-tokenizer
BuildRequires:  php-xmlwriter
BuildRequires:  phpunit10
# /oreon:deps
%description
PHP_CodeSniffer provides functionality to verify that code conforms to
certain standards, such as PEAR, or user-defined.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1 -b .rpm

%build

%install
: Install the library
mkdir -p                %{buildroot}%{pear_phpdir}/PHP/CodeSniffer
cp -pr src              %{buildroot}%{pear_phpdir}/PHP/CodeSniffer/src/
cp -pr autoload.php     %{buildroot}%{pear_phpdir}/PHP/CodeSniffer/
cp -pr requirements.php %{buildroot}%{pear_phpdir}/PHP/CodeSniffer/
cp -p  phpcs.xml.dist   %{buildroot}%{pear_phpdir}/PHP/CodeSniffer/
cp -p  phpcs.xsd        %{buildroot}%{pear_phpdir}/PHP/CodeSniffer/
: Cleanup
find %{buildroot}%{pear_phpdir}/PHP/CodeSniffer -depth -type d -name Tests -exec rm -r {} \; -print
: Install the commands
install -Dpm 755 bin/phpcs  %{buildroot}%{_bindir}/phpcs
install -Dpm 755 bin/phpcbf %{buildroot}%{_bindir}/phpcbf
%oreon_autofiles main
%if %{with tests}
%check

YEAR=$(date +%Y)
PREV=$(expr $YEAR - 1)
sed -e "/@copyright/s/${PREV}/${YEAR}/" \
    -i src/Standards/Squiz/Tests/Commenting/FileCommentUnitTest.1.*.fixed
ret=0
for cmdarg in \
    "php   %{phpunit}" \
    "php81 %{_bindir}/phpunit10" \
    "php82 %{_bindir}/phpunit11" \
    "php83 %{_bindir}/phpunit11" \
    "php84 %{_bindir}/phpunit11" \
    "php85 %{_bindir}/phpunit11"
  do if which $cmdarg; then
    set $cmdarg
    $1 -d memory_limit=-1 $2 \
       --filter '^((?!(testBrokenRulesetMultiError)).)*$' \
       --no-coverage || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
