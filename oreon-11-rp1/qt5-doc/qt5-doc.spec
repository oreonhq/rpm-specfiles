%global source0_hash ccceb68090754c60cbc09ebcd662a3224820fb4d1c9c3590ca45f8f14a98ab83
Name:    qt5-doc
Summary:        Qt5 - Complete documentation
Version: 5.15.16
Release:        1%{?dist}
BuildArch: noarch
License: LicenseRef-Callaway-GFDL
Url: http://qt-project.org/
Source0:        https://tarballs.oreonhq.com/qt-doc-opensource-src-%{version}.tar.xz
Source10:        generate-qt-doc.sh
%global debug_package   %{nil}
%global __spec_install_post %{nil}
Obsoletes: qt5-qtcanvas3d-doc < 5.13
Requires: qt5-qtbase-doc >= %{version}
Requires: qt5-qt3d-doc >= %{version}
Requires: qt5-qtcharts-doc >= %{version}
Requires: qt5-qtconnectivity-doc >= %{version}
Requires: qt5-qtdeclarative-doc >= %{version}
Requires: qt5-qtgraphicaleffects-doc >= %{version}
Requires: qt5-qtimageformats-doc >= %{version}
Requires: qt5-qtlocation-doc >= %{version}
Requires: qt5-qtmultimedia-doc >= %{version}
Requires: qt5-qtquickcontrols2-doc >= %{version}
Requires: qt5-qtquickcontrols-doc >= %{version}
Requires: qt5-qtscript-doc >= %{version}
Requires: qt5-qtscxml-doc >= %{version}
Requires: qt5-qtsensors-doc >= %{version}
Requires: qt5-qtserialbus-doc >= %{version}
Requires: qt5-qtserialport-doc >= %{version}
Requires: qt5-qtsvg-doc >= %{version}
Requires: qt5-qttools-doc >= %{version}
Requires: qt5-qtvirtualkeyboard-doc >= %{version}
Requires: qt5-qtwebchannel-doc >= %{version}
Requires: qt5-qtwebsockets-doc >= %{version}
Requires: qt5-qtx11extras-doc >= %{version}
Requires: qt5-qtxmlpatterns-doc >= %{version}
Requires: qt5-qtdatavis3d-doc >= %{version}
Requires: qt5-qtgamepad-doc >= %{version}
Requires: qt5-qtlocation-doc >= %{version}
Requires: qt5-qtwayland-doc >= %{version}
Requires: qt5-qtwebview-doc >= %{version}
Requires: qt5-qtspeech-doc >= %{version}
Requires: qt5-qtremoteobjects-doc >= %{version}
Requires: qt5-qtcharts-doc >= %{version}
Requires: qt5-qtpurchasing-doc >= %{version}
# oreon:deps
BuildRequires:  qt5-rpm-macros
# /oreon:deps
%description
This is the meta package for all Qt library documentation

# Empty files to produce qt5-doc package for easier installation of complete documentation
%package -n qt5-qtbase-doc
Summary: Documentation for qtbase
%description -n qt5-qtbase-doc
%{summary}.

%package -n qt5-qt3d-doc
Summary: Documentation for qt3d
%description -n qt5-qt3d-doc
%{summary}.

%package -n qt5-qtcharts-doc
Summary: Documentation for qtcharts
%description -n qt5-qtcharts-doc
%{summary}.

%package -n qt5-qtconnectivity-doc
Summary: Documentation for qtconnectivity
%description -n qt5-qtconnectivity-doc
%{summary}.

%package -n qt5-qtdeclarative-doc
Summary: Documentation for qtdeclarative
%description -n qt5-qtdeclarative-doc
%{summary}.

%package -n qt5-qtgraphicaleffects-doc
Summary: Documentation for qtgraphicaleffects
%description -n qt5-qtgraphicaleffects-doc
%{summary}.

%package -n qt5-qtimageformats-doc
Summary: Documentation for qtimageformats
%description -n qt5-qtimageformats-doc
%{summary}.

%package -n qt5-qtmultimedia-doc
Summary: Documentation for qtmultimedia
%description -n qt5-qtmultimedia-doc
%{summary}.

%package -n qt5-qtquickcontrols2-doc
Summary: Documentation for qtquickcontrols2
%description -n qt5-qtquickcontrols2-doc
%{summary}.

%package -n qt5-qtquickcontrols-doc
Summary: Documentation for qtquickcontrols
%description -n qt5-qtquickcontrols-doc
%{summary}.

%package -n qt5-qtscript-doc
Summary: Documentation for qtscript
%description -n qt5-qtscript-doc
%{summary}.

%package -n qt5-qtscxml-doc
Summary: Documentation for qtscxml
%description -n qt5-qtscxml-doc
%{summary}.

%package -n qt5-qtsensors-doc
Summary: Documentation for qtsensors
%description -n qt5-qtsensors-doc
%{summary}.

%package -n qt5-qtserialbus-doc
Summary: Documentation for qtserialbus
%description -n qt5-qtserialbus-doc
%{summary}.

%package -n qt5-qtserialport-doc
Summary: Documentation for qtserialport
%description -n qt5-qtserialport-doc
%{summary}.

%package -n qt5-qtsvg-doc
Summary: Documentation for qtsvg
%description -n qt5-qtsvg-doc
%{summary}.

%package -n qt5-qttools-doc
Summary: Documentation for qttools
%description -n qt5-qttools-doc
%{summary}.

%package -n qt5-qtvirtualkeyboard-doc
Summary: Documentation for qtvirtualkeyboard
%description -n qt5-qtvirtualkeyboard-doc
%{summary}.

%package -n qt5-qtwebchannel-doc
Summary: Documentation for qtwebchannel
%description -n qt5-qtwebchannel-doc
%{summary}.

%package -n qt5-qtwebsockets-doc
Summary: Documentation for qtwebsockets
%description -n qt5-qtwebsockets-doc
%{summary}.

%package -n qt5-qtx11extras-doc
Summary: Documentation for qtx11extras
%description -n qt5-qtx11extras-doc
%{summary}.

%package -n qt5-qtspeech-doc
Summary: Documentation for qtspeech
%description -n qt5-qtspeech-doc
%{summary}.

%package -n qt5-qtremoteobjects-doc
Summary: Documentation for qtremoteobjects
%description -n qt5-qtremoteobjects-doc
%{summary}.

%package -n qt5-qtpurchasing-doc
Summary: Documentation for qtpurchasing
%description -n qt5-qtpurchasing-doc
%{summary}.

%package -n qt5-qtwayland-doc
Summary: Documentation for qtwayland
%description -n qt5-qtwayland-doc
%{summary}.

%package -n qt5-qtwebview-doc
Summary: Documentation for qtwebview
%description -n qt5-qtwebview-doc
%{summary}.

%package -n qt5-qtlocation-doc
Summary: Documentation for qtlocation
%description -n qt5-qtlocation-doc
%{summary}.

%package -n qt5-qtxmlpatterns-doc
Summary: Documentation for qtxmlpatterns
%description -n qt5-qtxmlpatterns-doc
%{summary}.

%package -n qt5-qtdatavis3d-doc
Summary: Documentation for qtdatavis3d
%description -n qt5-qtdatavis3d-doc
%{summary}.

%package -n qt5-qtgamepad-doc
Summary: Documentation for qtgamepad
%description -n qt5-qtgamepad-doc
%{summary}.

%prep

# intentionally left blank
# though could be used to initially unpack (rex)

%build

%install
mkdir -p %{buildroot}
cat %{SOURCE0} %{SOURCE1} > qt-doc-opensource-src-%{version}.tar.xz
tar xf qt-doc-opensource-src-%{version}.tar.xz -C %{buildroot}
pushd %{buildroot}%{_qt5_docdir}
rm -rfv \
  qdoc* \
  qtdistancefieldgenerator* \
  qtdoc* qtcmake* \
  qtlottieanimation* \
  qtpdf* \
  qtwebengine*
popd
%oreon_autofiles qt5-qtbase-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qt3d-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtcharts-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtconnectivity-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtdeclarative-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtgraphicaleffects-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtimageformats-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtmultimedia-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtquickcontrols2-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtquickcontrols-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtscript-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtscxml-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtsensors-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtserialbus-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtserialport-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtsvg-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qttools-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtvirtualkeyboard-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtwebchannel-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtwebsockets-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtx11extras-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtspeech-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtremoteobjects-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtpurchasing-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtwayland-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtwebview-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtlocation-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtxmlpatterns-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtdatavis3d-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt5-qtgamepad-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-qtbase-doc -f %{oreon_filedir}/qt5-qtbase-doc.list
%files -n qt5-qt3d-doc -f %{oreon_filedir}/qt5-qt3d-doc.list
%files -n qt5-qtcharts-doc -f %{oreon_filedir}/qt5-qtcharts-doc.list
%files -n qt5-qtconnectivity-doc -f %{oreon_filedir}/qt5-qtconnectivity-doc.list
%files -n qt5-qtdeclarative-doc -f %{oreon_filedir}/qt5-qtdeclarative-doc.list
%files -n qt5-qtgraphicaleffects-doc -f %{oreon_filedir}/qt5-qtgraphicaleffects-doc.list
%files -n qt5-qtimageformats-doc -f %{oreon_filedir}/qt5-qtimageformats-doc.list
%files -n qt5-qtmultimedia-doc -f %{oreon_filedir}/qt5-qtmultimedia-doc.list
%files -n qt5-qtquickcontrols2-doc -f %{oreon_filedir}/qt5-qtquickcontrols2-doc.list
%files -n qt5-qtquickcontrols-doc -f %{oreon_filedir}/qt5-qtquickcontrols-doc.list
%files -n qt5-qtscript-doc -f %{oreon_filedir}/qt5-qtscript-doc.list
%files -n qt5-qtscxml-doc -f %{oreon_filedir}/qt5-qtscxml-doc.list
%files -n qt5-qtsensors-doc -f %{oreon_filedir}/qt5-qtsensors-doc.list
%files -n qt5-qtserialbus-doc -f %{oreon_filedir}/qt5-qtserialbus-doc.list
%files -n qt5-qtserialport-doc -f %{oreon_filedir}/qt5-qtserialport-doc.list
%files -n qt5-qtsvg-doc -f %{oreon_filedir}/qt5-qtsvg-doc.list
%files -n qt5-qttools-doc -f %{oreon_filedir}/qt5-qttools-doc.list
%files -n qt5-qtvirtualkeyboard-doc -f %{oreon_filedir}/qt5-qtvirtualkeyboard-doc.list
%files -n qt5-qtwebchannel-doc -f %{oreon_filedir}/qt5-qtwebchannel-doc.list
%files -n qt5-qtwebsockets-doc -f %{oreon_filedir}/qt5-qtwebsockets-doc.list
%files -n qt5-qtx11extras-doc -f %{oreon_filedir}/qt5-qtx11extras-doc.list
%files -n qt5-qtspeech-doc -f %{oreon_filedir}/qt5-qtspeech-doc.list
%files -n qt5-qtremoteobjects-doc -f %{oreon_filedir}/qt5-qtremoteobjects-doc.list
%files -n qt5-qtpurchasing-doc -f %{oreon_filedir}/qt5-qtpurchasing-doc.list
%files -n qt5-qtwayland-doc -f %{oreon_filedir}/qt5-qtwayland-doc.list
%files -n qt5-qtwebview-doc -f %{oreon_filedir}/qt5-qtwebview-doc.list
%files -n qt5-qtlocation-doc -f %{oreon_filedir}/qt5-qtlocation-doc.list
%files -n qt5-qtxmlpatterns-doc -f %{oreon_filedir}/qt5-qtxmlpatterns-doc.list
%files -n qt5-qtdatavis3d-doc -f %{oreon_filedir}/qt5-qtdatavis3d-doc.list
%files -n qt5-qtgamepad-doc -f %{oreon_filedir}/qt5-qtgamepad-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.16-4
- Import
