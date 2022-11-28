Name:		xkill
Version:	1.0.6
Release:	1
Summary:	Kill a client by its X resource
Group:		Monitoring
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source11:	%{name}-mini.png
Source12:	%{name}-std.png
Source13:	%{name}-large.png
License:	MIT
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xmu) >= 1.0.0

%description
Xkill is a utility for forcing the X server to close connections to clients.
This program is very dangerous, but is useful for aborting programs that have
displayed undesired windows on a user's screen.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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
NoDisplay=true
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/xkill.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/xkill.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/xkill.png

%files
%{_bindir}/xkill
%doc %{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/xkill.png
%{_iconsdir}/xkill.png
%{_liconsdir}/xkill.png
