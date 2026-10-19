%global source0_hash 29830aa84b049c7fe0c5b68157b283f0e549459592262c5eea605b6194b9f445
%global pkg pkg-info
Name:           emacs-%{pkg}
Version:        0.6
Release:        1%{?dist}
Summary:        Provide information about Emacs packages
License:        GPL-3.0-or-later
URL:            https://github.com/lunaryorn/%{pkg}.el/
Source0:        https://github.com/lunaryorn/%{pkg}.el//archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-epl
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs
BuildRequires:  emacs-epl
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version}

%build

%{_emacs_bytecompile} %{pkg}.el
%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
