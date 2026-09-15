%global source0_hash d9b99299f3fbd3070b357612f4a4c4c64bff59ad7f05b4e636efdf1b60fe69f6

Name:       cldr-emoji-annotation
Version:    48.2
Release:    %autorelease
%global tag_version release-%(echo %{version} | tr '~' '-' | tr '.' '-')
Summary:    Emoji annotation files in CLDR
License:    Unicode-DFS-2016
URL:        https://unicode.org/cldr
VCS:        git:https://github.com/unicode-org/cldr.git
Source0:    https://github.com/unicode-org/cldr/archive/refs/tags/%{tag_version}.tar.gz#/cldr-%{tag_version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libxml2
BuildArch:  noarch
Requires:  %{name}-dtd

%description
This package provides the emoji annotation file by language in CLDR.

%package dtd
Summary:    DTD files of CLDR common
Requires:   %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch:  noarch

%description dtd
This package contains DTD files of CLDR common which are required by
cldr-emoji-annotations.

%package devel
Summary:    Files for development using cldr-annotations
Requires:   %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:   pkgconfig
BuildArch:  noarch

%description devel
This package contains the pkg-config files for development
when building programs that use cldr-emoji-annotations.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n cldr-%{tag_version}


%install
pushd $PWD
ANNOTATION_DIR=common/annotations
CLDR_DIR=%{_datadir}/unicode/cldr/$ANNOTATION_DIR
pushd $ANNOTATION_DIR
for xml in *.xml ; do
    install -pm 644 -D $xml $RPM_BUILD_ROOT$CLDR_DIR/$xml
done
popd

ANNOTATION_DIR=common/annotationsDerived
CLDR_DIR=%{_datadir}/unicode/cldr/$ANNOTATION_DIR
pushd $ANNOTATION_DIR
for xml in *.xml ; do
    install -pm 644 -D $xml $RPM_BUILD_ROOT$CLDR_DIR/$xml
done
popd

DTD_DIR=common/dtd
CLDR_DIR=%{_datadir}/unicode/cldr/$DTD_DIR
pushd $DTD_DIR
for dtd in *.dtd ; do
    install -pm 644 -D $dtd $RPM_BUILD_ROOT$CLDR_DIR/$dtd
done
popd

install -pm 755 -d $RPM_BUILD_ROOT%{_datadir}/pkgconfig
cat >> $RPM_BUILD_ROOT%{_datadir}/pkgconfig/%{name}.pc <<_EOF
prefix=/usr

Name: cldr-emoji-annotations
Description: annotation files in CLDR
Version: %{version}
_EOF


%check
ANNOTATION_DIR=common/annotations
CLDR_DIR=%{_datadir}/unicode/cldr/$ANNOTATION_DIR
for xml in $ANNOTATION_DIR/*.xml ; do
    xmllint --noout --valid --postvalid $xml
done

ANNOTATION_DIR=common/annotationsDerived
CLDR_DIR=%{_datadir}/unicode/cldr/$ANNOTATION_DIR
for xml in $ANNOTATION_DIR/*.xml ; do
    xmllint --noout --valid --postvalid $xml
done


%files
%doc README.md
%license LICENSE
%{_datadir}/unicode/cldr/common/annotations
%{_datadir}/unicode/cldr/common/annotationsDerived

%files dtd
%dir %{_datadir}/unicode
%dir %{_datadir}/unicode/cldr
%dir %{_datadir}/unicode/cldr/common
%{_datadir}/unicode/cldr/common/dtd

%files devel
%{_datadir}/pkgconfig/*.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 48.2-1
- Prepare for Oreon 11 (RP1)
