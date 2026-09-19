%global source0_hash 6186b297e06686ff7a6f6b34dffe94ace827201861303b2180b6f68ac6337d10

%global commit      fb22eff1cde008dc009e738736d844bfd6c594f2
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       itop
Version:    0.1
Release:    25.20220502gitfb22eff1%{?dist}
Summary:    Interactive interrupt viewer

License:    MIT
URL:        https://github.com/kargig/%{name}
Source0:    https://github.com/kargig/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildArch:  noarch
BuildRequires:  perl-generators

%description
Interrupts 'top-like' utility for Linux

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{commit}

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
