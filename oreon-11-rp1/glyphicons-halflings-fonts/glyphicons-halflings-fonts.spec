%global source1_hash 13964e59d8e91ad8b02719bc498917a5ca09673ce24106267cf458c5972bb0fe
%global source0_hash bd18efd3efd70fec8ad09611a20cdbf99440b2c1d40085c29be036f891d65358
%global fontname glyphicons-halflings
%global githash 728067b586d2d989c07e8a6265f06fa8631c6b1f
%global gitshort 728067b
%global date 20140211
%global checkout %{date}git%{gitshort}
Name:           %{fontname}-fonts
Epoch:          1
Version:        5.3.8
Release:        1%{?dist}
Summary:        Precisely prepared monochromatic icons and symbols
License:        MIT
URL:            http://glyphicons.com/
Source0:        https://github.com/twbs/bootstrap/raw/%{githash}/fonts/%{fontname}-regular.ttf
Source1:        https://github.com/twbs/bootstrap/raw/%{githash}/LICENSE
BuildArch:      noarch
Requires:       fontpackages-filesystem
# oreon:deps
BuildRequires:  fontpackages-devel
BuildRequires:  ttembed
# /oreon:deps
%description
GLYPHICONS is a library of precisely prepared monochromatic icons and symbols,
created with an emphasis on simplicity and easy orientation.

%prep

ttembed %{SOURCE0}
install -m 0644 -p %{SOURCE1} LICENSE

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{buildroot}%{_fontdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
