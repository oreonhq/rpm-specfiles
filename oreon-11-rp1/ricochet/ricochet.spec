%global source0_hash f5f32caa3480def1de5c93010c6bf5f5789ddcba34bf09fc0feab67696d0c374

Name:		ricochet
Version:	1.1.4
Release:	39%{?dist}
Summary:	Anonymous peer-to-peer instant messaging

License:	BSD-3-Clause
URL:		https://ricochet.im/
Source0:	https://ricochet.im/releases/%{version}/ricochet-%{version}-src.tar.bz2
#Source0:	https://github.com/ricochet-im/%{name}/archive/1.1.3.tar.gz#/%{name}-1.1.3.tar.gz

BuildRequires: make
BuildRequires:	openssl-devel
BuildRequires:	protobuf-compiler
BuildRequires:	protobuf-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtbase-gui
BuildRequires:	qt5-qtdeclarative-devel
BuildRequires:	qt5-qtmultimedia-devel
BuildRequires:	qt5-qtquickcontrols
BuildRequires:	qt5-qttools-devel
BuildRequires:	desktop-file-utils
Requires:	tor hicolor-icon-theme
Requires:	qt5-qtquickcontrols

%description
Ricochet is an experiment with a different kind of instant messaging that
doesn't trust anyone with your identity, your contact list, or your
communications.
* You can chat without exposing your identity (or IP address) to anyone
* Nobody can discover who your contacts are or when you talk (meta-data-free!)
* There are no servers to compromise or operators to intimidate for your
     information
* It's cross-platform and easy for non-technical users

Warnings: Tor does no protocol cleaning.  That means there is a danger
that application protocols and associated programs can be induced to
reveal information about the initiator. Tor depends on Privoxy and
similar protocol cleaners to solve this problem. The present network
is very small -- this further reduces the strength of the anonymity
provided. Tor is not presently suitable for high-stakes anonymity.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

sed -i s/Qt/Qt\;/g src/ricochet.desktop

%build
%qmake_qt5 DEFINES+=RICOCHET_NO_PORTABLE CONFIG+=release
sed -i "s|\$(INSTALL_ROOT)/usr|\$(INSTALL_ROOT)%{_prefix}|g" Makefile.Release
make -f Makefile.Release %{?_smp_mflags}

%install
make -f Makefile.Release install INSTALL_ROOT=%{buildroot}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications src/ricochet.desktop

%files
%{_bindir}/ricochet
%{_datadir}/applications/ricochet.desktop
%{_datadir}/icons/hicolor/48x48/apps/ricochet.png
%exclude %{_datadir}/icons/hicolor/scalable/apps/ricochet.svg
%doc AUTHORS.md README.md
%license LICENSE

%changelog
%autochangelog
