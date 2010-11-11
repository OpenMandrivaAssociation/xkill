Name: xkill
Version: 1.0.3
Release: %mkrel 1
Summary: Kill a client by its X resource
Group: Monitoring
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source11:   %{name}-mini.png
Source12:   %{name}-std.png
Source13:   %{name}-large.png
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xkill is a utility for forcing the X server to close connections to clients.
This program is very dangerous, but is useful for aborting programs that have
displayed undesired windows on a user's screen.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=XKill
Comment=Kill a client by its X resource
Exec=/usr/bin/xkill
Icon=xkill
Terminal=false
Type=Application
StartupNotify=true
Categories=System;Monitor;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/xkill.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/xkill.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/xkill.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%{_bindir}/xkill
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/xkill.png
%{_iconsdir}/xkill.png
%{_liconsdir}/xkill.png
