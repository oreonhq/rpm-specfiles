%global source0_hash f9ebd05cd218b3c27d2763efd1b0bce7e6ccbade1396ce4e0f15a9f2bfb35aae
%global source2_hash 70da7140035621330f1b5ab6926197c3c3af467f2207d55a41f6396d9ad96abd
%global source3_hash 8b3e796574d63131fd3c90692c830ccf21a272433e3cc1b8c014979c84bd2ff4
%global codate 20190306
%global commit 4547332f0f27d98601a8f5732ce8e85e09dbdb93
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           gl-manpages
Version:        1.1
Release:        1%{?dist}
Summary:        OpenGL manpages
License:        Apache-2.0 AND HPND AND HPND-sell-variant AND MIT AND OpenPBS-2.3 AND SGI-B-2.0 AND W3C-19980720 AND X11
URL:            https://github.com/KhronosGroup/OpenGL-Refpages
Source0:        https://github.com/KhronosGroup/OpenGL-Refpages/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source2:        http://www.oasis-open.org/docbook/xml/mathml/1.1CR1/dbmathml.dtd
Source3:        http://www.w3.org/Math/DTD/mathml2.tgz
Source4:        gl-manpages-1.0.1.tar.bz2
Source5:        metainfo.xsl
BuildArch:      noarch
# oreon:deps
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook5-style-xsl
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  python3
# /oreon:deps
%description
OpenGL manpages

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
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
for MANP in `find gl-manpages-1.0.1 -name *.3gl` ; do
	FN=${MANP//*\//}
	cp -a --update=none $MANP $RPM_BUILD_ROOT%{_mandir}/man3/${FN/.3gl/.3G}
done
find $RPM_BUILD_ROOT%{_mandir}/man3/ -type f -size -100b | xargs sed -i -e 's/\.3gl/\.3G/' -e 's,^\.so man3G/,.so man3/,'
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
