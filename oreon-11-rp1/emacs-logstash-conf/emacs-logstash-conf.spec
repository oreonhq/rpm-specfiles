%global source0_hash ac2c803a0fc6b2ac526a98f19b62b9c31073acb89ef68ed97e6e07d1dc2ce34f

%global pkg logstash-conf

Name:           emacs-%{pkg}
Version:        0.4
Release:        12%{?dist}
Summary:        Emacs mode for editing Logstash configuration files

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/Wilfred/%{pkg}.el/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
A basic Emacs mode for editing Logstash configuration files.

Features:
  * Syntax highlighting
  * Indentation

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}.el-%{version}

%build
%{_emacs_bytecompile} %{pkg}.el

%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el

%files
%doc README.md
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el

%changelog
%autochangelog
