%global source2_hash 70da7140035621330f1b5ab6926197c3c3af467f2207d55a41f6396d9ad96abd
%global source0_hash none
%global source3_hash 8b3e796574d63131fd3c90692c830ccf21a272433e3cc1b8c014979c84bd2ff4
%global source4_hash 90ec9bcd8a518425513076f10fa14d90f19ca430940e01e497f0ce80fdd0fd03

# FIXME:  Figure out what to do about the gles* manpages, maybe different conflicting packages...
%global codate 20190306
%global commit 4547332f0f27d98601a8f5732ce8e85e09dbdb93
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gl-manpages
Version:        1.1
Release:        35.%{codate}%{?dist}
Summary:        OpenGL manpages

# This package uses SGI-B-1.1, we choose to use later variant of this license
# becase SGI-B-1.1 is not allowed, but it allows to use later variants and
# that is allowed
License:        Apache-2.0 AND HPND AND HPND-sell-variant AND MIT AND OpenPBS-2.3 AND SGI-B-2.0 AND W3C-19980720 AND X11
URL:            https://github.com/KhronosGroup/OpenGL-Refpages
Source0:        https://github.com/KhronosGroup/OpenGL-Refpages/archive/%{commit}/%{name}-%{shortcommit}.tar.gz#/gl-manpages-1.1.tar.gz
# FIXME: Bundle mathml and the Oasis dbmathl until they are packaged
Source2:        https://www.oasis-open.org/docbook/xml/mathml/1.1CR1/dbmathml.dtd
Source3:        https://www.w3.org/Math/DTD/mathml2.tgz
# FIXME  These are the old gl-manpages source which 
# still have some manpages that khronos doesn't. 
# Ship until somebody in the know helps figuring whats what.
# When matching install the khronos version.
Source4:        https://gitlab.freedesktop.org/mesa/gl-manpages/-/archive/main/gl-manpages-main.tar.bz2#/gl-manpages-1.0.1.tar.bz2
#Silence author/version/manual etc. warnings
Source5:        metainfo.xsl

BuildArch:      noarch

BuildRequires: make
BuildRequires:  libxslt docbook-style-xsl docbook5-style-xsl python3

%description
OpenGL manpages

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
%setup -q -n OpenGL-Refpages-%{commit}
tar xzf %{SOURCE3}
cp -av %{SOURCE2} mathml2/
tar xjf %{SOURCE4}


%build
export BD=`pwd`
xmlcatalog --create --noout \
	--add public "-//W3C//DTD MathML 2.0//EN" "file://$BD/mathml2/mathml2.dtd" \
	--add system "http://www.w3.org/TR/MathML2/dtd/mathml2.dtd" "file://$BD/mathml2/mathml2.dtd" \
	--add public "-//OASIS//DTD DocBook MathML Module V1.1b1//EN" "file://$BD/mathml2/dbmathml.dtd" \
	--add system "http://www.oasis-open.org/docbook/xml/mathml/1.1CR1/dbmathml.dtd" "file://$BD/mathml2/dbmathml.dtd" \
	mathml2.cat
export XML_CATALOG_FILES="$BD/mathml2.cat /etc/xml/catalog"
make
pushd gl4
	for MANP in gl*.xml ; do
		xsltproc --xinclude --nonet %{SOURCE5} $MANP | xsltproc --xinclude --nonet /usr/share/sgml/docbook/xsl-ns-stylesheets/manpages/docbook.xsl -
	done
popd


%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3/
cp -n gl4/*.3G $RPM_BUILD_ROOT%{_mandir}/man3/
# install the old manpages source with 3gl -> 3G
# when matchin don't clobber the khronos version
for MANP in `find gl-manpages-1.0.1 -name *.3gl` ; do
	FN=${MANP//*\//}
	cp -a --update=none $MANP $RPM_BUILD_ROOT%{_mandir}/man3/${FN/.3gl/.3G}
done
find $RPM_BUILD_ROOT%{_mandir}/man3/ -type f -size -100b | xargs sed -i -e 's/\.3gl/\.3G/' -e 's,^\.so man3G/,.so man3/,'


%files
%{_mandir}/man3/*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-35.20190306
- Import
