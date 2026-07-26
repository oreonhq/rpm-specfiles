%global source0_hash 3d20e7c35231dff2fc9282e59c1ece7a89a9243657e6399bdd6dd530f1588a63

Name:           newflasher
Version:        59
Release:        %autorelease
Summary:        Flash tool for new Sony flash tool protocol (Xperia XZ Premium and further)

License:        MIT
URL:            https://github.com/munjeni/newflasher
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  zlib-ng-compat-devel

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build

%install
install -Dpm 0755 newflasher %{buildroot}/%{_bindir}/newflasher
install -Dpm 0644 newflasher.1 %{buildroot}/%{_mandir}/man1/newflasher.1

%files
%doc readme.md
%{_bindir}/newflasher
%{_mandir}/man1/newflasher.1.*

%changelog
%autochangelog
