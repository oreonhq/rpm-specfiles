%global source0_hash 5aba83a07b514ef9b44178ed392f86cfbbd2319d2b379c7d55f38de81e8c5e4f

%global jsname jsroot

Name:		js-%{jsname}
Version:	7.10.3
Release:	1%{?dist}
Summary:	JavaScript ROOT - Interactive numerical data analysis graphics

#		Most files are MIT, d3.mjs is BSD, dat.gui.mjs is Apache-2.0
License:	MIT AND BSD-3-Clause AND Apache-2.0
URL:		https://jsroot.gsi.de/
Source0:	https://github.com/root-project/%{jsname}/archive/%{version}/%{jsname}-%{version}.tar.gz
#		Use locally installed mathjax instead of remote installation.
Patch0:		%{name}-mathjax.patch

BuildArch:	noarch
BuildRequires:	dos2unix
BuildRequires:	web-assets-devel
Requires:	web-assets-filesystem
Requires:	mathjax3

%description
JavaScript ROOT provides interactive ROOT-like graphics in web browsers.
Data can be read and displayed from binary and JSON ROOT files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{jsname}-%{version}
%patch -P0 -p1

dos2unix -k modules/base/jspdf.mjs modules/base/svg2pdf.mjs

%build
# nothing to do

%install
mkdir -p %{buildroot}%{_jsdir}/%{jsname}

# In upstream's released version modules/d3.mjs and modules/three.mjs
# are minified, but in root's bundled version they ar not.
# Leave them unminified in Fedora.
for d in modules modules/base modules/draw modules/geom modules/gpad \
    modules/gui modules/hist modules/hist2d ; do
mkdir %{buildroot}%{_jsdir}/%{jsname}/${d}
install -m 644 -p ${d}/*.mjs %{buildroot}%{_jsdir}/%{jsname}/${d}
done

ln -rs %{buildroot}%{_jsdir}/mathjax@3 %{buildroot}%{_jsdir}/%{jsname}/mathjax

mkdir %{buildroot}%{_jsdir}/%{jsname}/build
install -m 644 -p build/jsroot.js %{buildroot}%{_jsdir}/%{jsname}/build

mkdir %{buildroot}%{_jsdir}/%{jsname}/scripts
install -m 644 -p scripts/*.js %{buildroot}%{_jsdir}/%{jsname}/scripts

# Upstream's released version adds a copy with the ending .min.js
# Despite its name it is not minified. Do the same for Fedora.
ln %{buildroot}%{_jsdir}/%{jsname}/scripts/JSRoot.core.js \
   %{buildroot}%{_jsdir}/%{jsname}/scripts/JSRoot.core.min.js

mkdir -p %{buildroot}%{_jsdir}/%{jsname}/files
install -m 644 -p files/* %{buildroot}%{_jsdir}/%{jsname}/files

mkdir -p %{buildroot}%{_jsdir}/%{jsname}/img
install -m 644 -p img/* %{buildroot}%{_jsdir}/%{jsname}/img

mkdir -p %{buildroot}%{_pkgdocdir}
ln -rs %{buildroot}%{_jsdir}/%{jsname}/build %{buildroot}%{_pkgdocdir}
ln -rs %{buildroot}%{_jsdir}/%{jsname}/img %{buildroot}%{_pkgdocdir}
ln -rs %{buildroot}%{_jsdir}/%{jsname}/modules %{buildroot}%{_pkgdocdir}
ln -rs %{buildroot}%{_jsdir}/%{jsname}/scripts %{buildroot}%{_pkgdocdir}

%pretrans -p <lua>
-- Remove links created by broken scriptlet in root-net-http
linkstoremove = {
  "%{_jsdir}/%{jsname}/img/img",
  "%{_jsdir}/%{jsname}/libs/libs",
  "%{_jsdir}/%{jsname}/scripts/scripts",
  "%{_jsdir}/%{jsname}/style/style"
}
for _, path in ipairs(linkstoremove) do
  st = posix.stat(path)
  if st and st.type == "link" then
    os.remove(path)
  end
end

%files
%{_jsdir}/%{jsname}
%license LICENSE libs/*.LICENSE
%doc %{_pkgdocdir}/*
%doc changes.md demo docs/* index.htm readme.md

%changelog
%autochangelog
