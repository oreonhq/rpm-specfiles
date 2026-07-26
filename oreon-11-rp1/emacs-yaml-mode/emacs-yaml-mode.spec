%global source0_hash 07d2aee94aa23a7973f8d0d64fe5ebedac0f42b8f7b2022a899f71cd14a09bfc

%global pkg yaml-mode

Name:      emacs-%{pkg}
Version:   0.0.16
Release:   6%{?dist}
Summary:   Major mode to edit YAML files for emacs
License:   GPL-3.0-or-later
URL:       https://github.com/yoshiki/yaml-mode
Source0:   https://github.com/yoshiki/%{pkg}/archive/%{version}.tar.gz
Source1:   yaml-mode-init.el
BuildArch: noarch
Requires:  emacs(bin) >= %{_emacs_version}
BuildRequires: emacs
BuildRequires: make

%description
Major mode to edit YAML files for emacs

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkg}-%{version}

%build
make PREFIX=%{_prefix} %{?_smp_mflags}

%check
make test

%install
mkdir -p %{buildroot}/%{_emacs_sitelispdir}/%{pkg}
make install PREFIX=%{_prefix} INSTALLLIBDIR=%{buildroot}%{_emacs_sitelispdir}/%{pkg}

mkdir -p %{buildroot}/%{_emacs_sitestartdir}
install -pm 644 %SOURCE1 %{buildroot}%{_emacs_sitestartdir}

%files
%doc README Changes
%license LICENSE.txt
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el

%changelog
%autochangelog
