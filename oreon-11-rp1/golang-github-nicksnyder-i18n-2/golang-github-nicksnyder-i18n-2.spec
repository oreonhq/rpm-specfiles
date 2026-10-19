%global source0_hash 4c1f8febe1ec7e36e0716c3a06c57a2b74980bfeceb4e898e4fdb8b602d87eba
%bcond check 0
%global goipath         github.com/nicksnyder/go-i18n/v2
%global forgeurl        https://github.com/nicksnyder/go-i18n
Version:                2.1.2
%gometa
%global common_description %{expand:
go-i18n is a Go package and a command that helps you translate Go programs into
multiple languages.
 - Supports pluralized strings for all 200+ languages in the Unicode Common
   Locale Data Repository (CLDR).
    - Code and tests are automatically generated from CLDR data.
 - Supports strings with named variables using text/template syntax.
 - Supports message files of any format (e.g. JSON, TOML, YAML, etc.).
 - Documented and tested!}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md dev.md example
Name:           %{goname}
Release:        1%{?dist}
Summary:        Translate your Go program into multiple languages
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/go-i18n-%{version}.tar.gz
Patch0:         0001-Fix-error-message-changed-with-Go-1.16.patch
Provides:       go-i18n = %{version}-%{release}
Obsoletes:      go-i18n < 1.10.0-7
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(golang.org/x/text/language)
BuildRequires:  golang(gopkg.in/yaml.v2)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1
mv v2/* ./

%build

for cmd in goi18n; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
