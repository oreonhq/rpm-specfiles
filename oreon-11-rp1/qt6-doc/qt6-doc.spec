Name:    qt6-doc
Summary: Qt6 - Complete documentation
Version: 6.9.1
Release: 6%{?dist}
BuildArch: noarch

License: GFDL
# The tarball is a pre-assembled install tree of Qt docs (qch, html, tags). Qt does not publish this
# file name on download.qt.io. Generate with Source1 or copy Source0 out of a Fedora qt6-doc SRPM
# (rpm2cpio *.src.rpm | cpio -idmv). Host it on your lookaside if spectool must fetch by URL.
Url:     http://qt-project.org/
Source0: qt-doc-opensource-src-%{version}.tar.xz
Source1: generate-qt6-doc.sh
Source2: qtbase-tell-the-truth-about-private-API.patch

# optimize build, skip unecessary steps
%global debug_package   %{nil}
%global __spec_install_post %{nil}

BuildRequires: qt6-rpm-macros

%description
Documentation for Qt6 API in QCH format
%{summary}.

%package html
Summary: Qt API Documentation in HTML format

%description html
%{summary}.


%package devel
Summary: tags files for crosslinking to Qt QCH files

%description devel
%{summary}.


%prep
# intentionally left blank
# though could be used to initially unpack (rex)


%build
# intentionally left blank


%install
mkdir -p %{buildroot}
tar xf %{SOURCE0} -C %{buildroot}

%files
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%files devel
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%changelog
* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.9.1-6
- Document how to obtain Source0 prebuilt doc tarball when no public URL exists

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.9.1-5
- bump release (retry failed build)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.9.1-4
- Prepare for Oreon 11 (RP1)
