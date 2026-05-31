%global source0_hash 415c3c7da62fe3b2ad1e524df342f1c534330ed5fa579bfe7127150e9a364b49

Name:    qt6-doc
Summary: Qt6 - Complete documentation
Version: 6.9.1
Release: 7%{?dist}
BuildArch: noarch

License: GFDL
# Pre-assembled doc install tree (qch, html, tags). Qt does not ship this as one tarball on download.qt.io.
# This URL is Fedora lookaside for qt6-doc (same blob as in their SRPM). When bumping %%version, refresh
# %%qt_doc_tarball_sha512 from https://src.fedoraproject.org/rpms/qt6-doc/raw/rawhide/f/sources
# or run Source1 generate-qt6-doc.sh and host the file yourself.
%global qt_doc_tarball_sha512 fc6867d4a94e309c1b7ca4d167837833c342a55db6830e440f4a13ce21cc2a0edac9ed1f531959e963ccb10f4514aa27e9e5ffa360873d5f9203f6e5e3eaa8f6
Url:     http://qt-project.org/
Source0:        https://src.fedoraproject.org/repo/pkgs/rpms/qt6-doc/qt-doc-opensource-src-6.9.1.tar.xz/sha512/fc6867d4a94e309c1b7ca4d167837833c342a55db6830e440f4a13ce21cc2a0edac9ed1f531959e963ccb10f4514aa27e9e5ffa360873d5f9203f6e5e3eaa8f6/qt-doc-opensource-src-6.9.1.tar.xz
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }# intentionally left blank
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
* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.9.1-7
- Source0 HTTPS URL on Fedora lookaside (spectool friendly)

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.9.1-6
- Document how to obtain Source0 prebuilt doc tarball when no public URL exists

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.9.1-5
- bump release (retry failed build)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.9.1-4
- Prepare for Oreon 11 (RP1)
