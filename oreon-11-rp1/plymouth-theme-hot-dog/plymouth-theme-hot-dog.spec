%global source0_hash 272bd190b883a6ef3b273a210cdbfcbb7d10a248a399a5f64b2cf52b715456bf

%define themename hot-dog
%define set_theme %{_sbindir}/plymouth-set-default-theme
Name:           plymouth-theme-%{themename}
Version:        0.5
Release:        31%{?dist}
Summary:        Plymouth Happy Hot Dog Theme

# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            http://wwoods.fedorapeople.org/hot-dog/
Source0:        %{name}-%{version}.tar.bz2
BuildArch:      noarch
Requires:       plymouth-plugin-two-step >= 0.7.0
Requires(post): plymouth-scripts

%description
This package contains the Happy Hot Dog boot splash theme for Plymouth.
The mustard indicates progress.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# nada

%install
targetdir=$RPM_BUILD_ROOT/%{_datadir}/plymouth/themes/%{themename}
rm -rf $RPM_BUILD_ROOT
install -d -m 0755 $targetdir
install -m 0644 %{themename}.plymouth *.png $targetdir

%post
export LIB=%{_lib}
# on initial install, set this as the new theme
if [ $1 -eq 1 ]; then
    %{set_theme} %{themename}
fi

%postun
export LIB=%{_lib}
# if uninstalling, reset to boring meatless default theme
if [ $1 -eq 0 ]; then
    if [ "$(%{set_theme})" == "%{themename}" ]; then
        %{set_theme} --reset
    fi
fi

%files
%doc README
%dir %{_datadir}/plymouth/themes/%{themename}
%{_datadir}/plymouth/themes/%{themename}/*.png
%{_datadir}/plymouth/themes/%{themename}/%{themename}.plymouth

%changelog
%autochangelog
