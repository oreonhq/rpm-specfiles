%global source0_hash 47ea016b8f6b05d15ba5e12e1773eeca9cea13f79fd73cd44f6873f1f276db0e

%global pkg dockerfile-mode

Name:           emacs-%{pkg}
Version:        1.9
Release:        5%{?dist}
Summary:        An emacs mode for handling Dockerfiles

License:        Apache-2.0
URL:            https://github.com/spotify/%{pkg}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
BuildRequires:  emacs-s
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-s
BuildArch:      noarch

%description
This package provides a major mode `dockerfile-mode' for use with the standard
`Dockerfile' file format.  Additional convenience functions allow images to be
built easily.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version}

%build
%{_emacs_bytecompile} %{pkg}.el

%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el

%files
%doc README.md
%license LICENSE
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el

%changelog
%autochangelog
