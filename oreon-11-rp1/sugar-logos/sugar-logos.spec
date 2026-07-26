%global source0_hash 3ba15729f26deb8415489e000cf81be4f567157b8d2fb37793b651aea6ecb4af

Name:           sugar-logos
Version:        3
Release:        32%{?dist}
Summary:        Boot splash imagery for Sugar on a Stick

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/sugarlabs/sugar-logos.git
Source0:        http://download.sugarlabs.org/sources/external/sugar-logos/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  plymouth-theme-charge
Requires:       plymouth
Requires:       plymouth-plugin-two-step

%description
A boot splash screen for Sugar using Plymouth.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/sugar/
for i in src/* ; do
    install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/sugar/
done

cp %{_datadir}/plymouth/themes/charge/{box,bullet,entry,lock}.png $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/sugar

%post
export LIB=%{_lib}
if [ $1 -eq 1 ]; then
    %{_sbindir}/plymouth-set-default-theme sugar
else
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "solar" ]; then
        %{_sbindir}/plymouth-set-default-theme sugar
    fi
fi

%postun
export LIB=%{_lib}
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "sugar" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

%files
%license COPYING
%doc AUTHORS
%{_datadir}/plymouth/themes/sugar/

%changelog
%autochangelog
