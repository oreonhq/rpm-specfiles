%global source0_hash none

Name:           tremulous-data
Version:        1.2.0
Release:        0.30.beta1%{?dist}
Summary:        Data files for tremulous the FPS game

# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            http://tremulous.net
# To get the source tarball:
# wget http://downloads.sourceforge.net/tremulous/tremulous-1.1.0.zip
# unzip tremulous-1.1.0.zip
# wget http://prdownloads.sourceforge.net/tremulous/tremulous-gpp1.zip
# unzip tremulous-gpp1.zip
# cp tremulous/gpp/* tremulous/base/
# mkdir tremulous-data-1.2.0
# cp tremulous/base tremulous-data-1.2.0/
# cp tremulous/C* tremulous-data-1.2.0/
# cp tremulous/manual.pdf tremulous-data-1.2.0/
# tar -czf tremulous-data-1.2.0.tar.gz tremulous-data-1.2.0
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-copyright.txt
BuildArch:      noarch

%description
Data files for tremulous the Quake 3 based FPS game.

%prep
%setup -q
install -p -m 644 %{SOURCE1} fedora-copyright.txt

# %build
# nothing to build data only

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/tremulous/base
install -p -m 0644 base/*.pk3 $RPM_BUILD_ROOT%{_datadir}/tremulous/base/
install -p -m 0644 base/*.cfg $RPM_BUILD_ROOT%{_datadir}/tremulous/base/

%files
%license CC COPYING fedora-copyright.txt
%doc manual.pdf
%{_datadir}/tremulous

%changelog
%autochangelog
