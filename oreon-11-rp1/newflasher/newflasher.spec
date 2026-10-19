%global source0_hash d6d9db74b96393fba820996ee561c5c0f7283bed498f21360bd61033c8576bdd
Name:           newflasher
Version:        60
Release:        1%{?dist}
Summary:        Flash tool for new Sony flash tool protocol (Xperia XZ Premium and further)
License:        MIT
URL:            https://github.com/munjeni/newflasher
Source0:        https://github.com/munjeni/%{name}/archive/refs/tags/%{version}.tar.gz
# oreon:deps
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  zlib-ng-compat-devel
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
install -Dpm 0755 newflasher %{buildroot}/%{_bindir}/newflasher
install -Dpm 0644 newflasher.1 %{buildroot}/%{_mandir}/man1/newflasher.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
