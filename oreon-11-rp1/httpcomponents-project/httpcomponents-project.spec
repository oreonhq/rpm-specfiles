%bcond_with bootstrap

Name:           httpcomponents-project
Version:        13
Release:        %autorelease
Summary:        Common POM file for HttpComponents
License:        Apache-2.0
URL:            https://hc.apache.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://archive.apache.org/dist/httpcomponents/httpcomponents-parent/httpcomponents-parent-%{version}-source-release.zip
# oreon url source checksums begin
%global source0_sha256 3b633734fbcc02940fc3c16d1dc7a6e48f342d146e980012facf7583d4096d62
%global source0_file httpcomponents-parent-13-source-release.zip
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif

%description
Common Maven POM file for HttpComponents. This project should be
required only for building dependant packages with Maven. Please don't
use it as runtime requirement.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/httpcomponents-parent-13-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3b633734fbcc02940fc3c16d1dc7a6e48f342d146e980012facf7583d4096d62" || { echo "oreon: Source0 SHA256 mismatch for httpcomponents-parent-13-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -C

%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :apache-rat-plugin

# Version <= 8 had this AID
%mvn_alias : :project

%build
%mvn_file  : %{name}
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13-1
- Import
