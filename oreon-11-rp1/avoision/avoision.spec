%global source0_hash 353b774ca234c8dde2625f14ea76057d2adc30a64805650da8647c94ef9b9651
Name:		avoision
Version:	1.1
Release:        1%{?dist}
Summary:        Arcade style game of evade and capture
License:	GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:		http://avsn.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/avsn/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Source2:	%{name}.desktop
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  radius-engine-devel
BuildRequires:  zip
# /oreon:deps
%description
Avoision is a straightforward, yet captivating distillation of vintage arcade 
entertainment requiring strategy, precision, and perseverance with a singular 
objective: capture the red square while evading innumerable cruel, spiteful 
white squares.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
chmod -x License.txt ChangeLog *.c

%build

%configure
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications	%{SOURCE2}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
