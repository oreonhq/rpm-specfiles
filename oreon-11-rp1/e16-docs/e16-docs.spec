%global source0_hash b8d8e0caf45931ce672fa5088a963685533a65a9a8cfeee15239d96f3b91593f

Summary:   Documentation for Enlightenment, DR16
Name:      e16-docs
Version:   0.16.8.0.2
Release:   32%{?dist}
# Automatically converted from old format: MIT with advertising - review is highly recommended.
License:   LicenseRef-Callaway-MIT-with-advertising
URL:       http://www.enlightenment.org/
Source:    http://downloads.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: make
Requires:  e16 >= 0.16.8 dejavu-sans-fonts

%description
This package contains documentation for Enlightenment, DR16.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
%{__make} %{?_smp_mflags} 

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot} INSTALL="%{__install} -p"

%files
%doc AUTHORS COPYING README
%{_datadir}/e16/E-docs

%changelog
%autochangelog
