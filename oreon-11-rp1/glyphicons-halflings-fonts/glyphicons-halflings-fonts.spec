%global source0_hash none

%global fontname glyphicons-halflings
%global githash 728067b586d2d989c07e8a6265f06fa8631c6b1f
%global gitshort 728067b
%global date 20140211
%global checkout %{date}git%{gitshort}

Name:           %{fontname}-fonts
Epoch:          1
Version:        3.1.0
Release:        25.%{checkout}%{?dist}
Summary:        Precisely prepared monochromatic icons and symbols

License:        MIT
URL:            http://glyphicons.com/

Source0:        https://github.com/twbs/bootstrap/raw/%{githash}/fonts/glyphicons-halflings-regular.ttf
Source1:        https://github.com/twbs/bootstrap/raw/%{githash}/LICENSE
BuildArch:      noarch
BuildRequires:  fontpackages-devel 
BuildRequires:  ttembed
Requires:       fontpackages-filesystem

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

%files
%doc LICENSE
%{_fontdir}

%changelog
%autochangelog
