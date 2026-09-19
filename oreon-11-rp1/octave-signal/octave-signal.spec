%global source0_hash 6a8b4b8cf0b3019d984fde75af947ae73e9a1c509890552cd5e113f7ba89038c

%global octpkg signal

Name:           octave-%{octpkg}
Version:        1.4.7
Release:        1%{?dist}
Summary:        Signal processing tools for Octave
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://octave.sourceforge.net/signal/
Source0:        https://github.com/gnu-octave/%{name}/releases/download/%{version}/%{octpkg}-%{version}.tar.gz

# buildsys seems broken for s390x
ExcludeArch:    s390x

# currently no octave-control on aarch64
ExcludeArch:    aarch64

BuildRequires:  octave-devel >= 6:3.8.0
BuildRequires:  octave-control >= 2.4.5

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
Requires:       octave-control >= 2.4.5

%description
Signal processing tools, including filtering, windowing and display

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{octpkg}-%{version}
for i in inst/*.m; do
  iconv -f iso8859-1 -t utf-8 $i > $i.conv && mv -f $i.conv $i
done;

%build
#octave pkg build dependency check does not work
#https://bugzilla.redhat.com/show_bug.cgi?id=733615
%octave_pkg_build
#octave_cmd pkg build '-verbose' '-nodeps' %{_tmppath}/%{name}-%{version}-%{release}.%{_arch} %{_builddir}/%{buildsubdir}

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}

%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/private/*.m
%{octpkgdir}/packinfo
%{_metainfodir}/io.sourceforge.octave.signal.metainfo.xml
%{octpkgdir}/PKG_ADD
%{octpkgdir}/PKG_DEL
%doc %{octpkgdir}/doc
%{octpkgdir}/compatibility/pre-11.0.0

%changelog
%autochangelog
