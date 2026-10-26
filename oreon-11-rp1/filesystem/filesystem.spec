%global debug_package %{nil}

Name: filesystem
Version: 11
Release: 4%{?dist}
Summary: Base directory layout
License: MIT
URL: https://oreonhq.com/
Provides: filesystem(unmerged-sbin-symlinks)

%description
The directories and compatibility symlinks every other package installs into.

%pretrans -p <lua>
local function ensure_dir(path)
  if posix.stat(path, "type") == nil then
    posix.mkdir(path)
  end
end
local function ensure_link(path, target)
  local st = posix.stat(path, "type")
  if st == "directory" then
    local ok, err = os.rename(path, path .. ".rpmmoved")
    if not ok then
      error("rename " .. path .. " failed: " .. tostring(err))
    end
    st = nil
  end
  if st == nil then
    local ok, err = posix.symlink(target, path)
    if not ok then
      error("symlink " .. path .. " failed: " .. tostring(err))
    end
  end
end
ensure_dir("/usr")
ensure_dir("/usr/bin")
ensure_dir("/usr/sbin")
ensure_dir("/usr/lib")
ensure_dir("/usr/lib64")
ensure_link("/bin", "usr/bin")
ensure_link("/sbin", "usr/bin")
ensure_link("/lib", "usr/lib")
ensure_link("/lib64", "usr/lib64")

%prep
:

%build
:

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libexecdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_mandir}
mkdir -p %{buildroot}%{_infodir}
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/usr/lib
mkdir -p %{buildroot}/var
mkdir -p %{buildroot}/var/tmp
mkdir -p %{buildroot}/var/log
mkdir -p %{buildroot}/var/cache
mkdir -p %{buildroot}/run
mkdir -p %{buildroot}/proc
mkdir -p %{buildroot}/sys
mkdir -p %{buildroot}/tmp
mkdir -p %{buildroot}/boot
mkdir -p %{buildroot}/home
mkdir -p %{buildroot}/root
chmod 1777 %{buildroot}/tmp %{buildroot}/var/tmp
ln -s usr/bin %{buildroot}/bin
ln -s usr/bin %{buildroot}/sbin
ln -s usr/lib %{buildroot}/lib
ln -s usr/lib64 %{buildroot}/lib64

%files
%dir /usr
%dir %{_bindir}
%dir %{_sbindir}
%dir /usr/sbin
%dir /usr/lib
%dir %{_libdir}
%dir %{_libexecdir}
%dir %{_includedir}
%dir %{_datadir}
%dir %{_sysconfdir}
%dir %{_mandir}
%dir %{_infodir}
%dir /var
%dir /var/tmp
%dir /var/log
%dir /var/cache
%dir /run
%dir /proc
%dir /sys
%dir /tmp
%dir /boot
%dir /home
%dir /root
/bin
/sbin
/lib
/lib64
