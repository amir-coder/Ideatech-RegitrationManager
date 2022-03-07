from email.policy import default
import enum

class Role(enum.Enum):
    trainer = 'trainer'
    orgenizer = 'orgenizer'
    in_comp = 'in_comp'
    in_workshop = 'in_workshop'
    vip = 'vip'
    default = 'in_comp'